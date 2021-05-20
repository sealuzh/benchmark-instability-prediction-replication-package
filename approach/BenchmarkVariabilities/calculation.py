# With this .py file, we calculate the mean and CV of the benchmarks

# 1) mean
# 2) coefficient of variation (CV)

from statistics import mean, median, stdev, quantiles, variance
import csv, re
from scipy.stats import norm
from scipy.stats.mstats import mjci, hdmedian, hdquantiles

import numpy

numpy.seterr('raise')

def calculate_mean(list):
    """
    returns mean of a list in float
    :param list:
    :return:
    """
    if len(list) < 2:
        return -1
    else:
        return mean(list)

def calculate_CV(list):
    """
    returns coefficient of variation of a list in float
    :param list:
    :return:
    """
    if len(list) < 2:
        return -1
    else:
        return 0.0 if variance(list) == 0.0 else (stdev(list)/mean(list)) * 100

# MAD coefficients for bias-correction
# taken from https://doi.org/10.1080/03610918.2019.1699114 (values from https://aakinshin.net/posts/unbiased-mad/#Hampel1974)
mad_coefficient = {
    -1: 1.4826,
    5: 1.803927,
    10: 1.624681,
    20: 1.545705,
    30: 1.523031,
}

def calculate_RMAD(list, samples = -1):
    """
    returns the relative median absolute deviation, which normalizes the MAD by the median
    (see https://en.wikipedia.org/wiki/Median_absolute_deviation)
    
    :param list:
    :return:
    """
    if len(list) < 2:
        return -1
    
    med = median(list)
    if med == 0:
        return 0.0
    mad = median([abs(e - med) for e in list])
    return (mad_coefficient[samples] * mad / med) * 100

def calculate_RMAD_HD(list, samples = -1):
    """
    returns the relative median absolute deviation, which normalizes the MAD by the median
    (see https://en.wikipedia.org/wiki/Median_absolute_deviation)
    it estimates the median based on the Harrald-Davis quantile estimator
    
    :param list:
    :return:
    """
    if len(list) < 2:
        return -1
    
    med = hdmedian(list)
    med = round(med.compressed()[0], 5)
    if med == 0:
        return 0.0
    
    mad = round(hdmedian([abs(e - med) for e in list]).compressed()[0], 5)
    return (mad_coefficient[samples] * mad / med) * 100

def calculate_COQV(list, n = 4, q1 = 0, q2 = 2):
    """
    returns the quantile coefficient of dispersion
    (see https://en.wikipedia.org/wiki/Quartile_coefficient_of_dispersion)

    :param list:
    :param q1:
    :param q2:
    :return:
    """
    if len(list) < 2:
        return -1
    elif q1 >= q2 or (q2 - 1) >= n:
        raise Exception("invalid parameters n = {0}, q1 = {1}, q2 = {2}".format(n, q1, q2))

    
    qs = [round(q, 1) for q in quantiles(list, n=n)]
    q1v = qs[q1]
    q2v = qs[q2]
    return (q2 - q1) / (q2 + q1)

def calculate_RCIW_MJ_HD(data, prob = 0.5, alpha = 0.01, axis = None):
    """
    Computes the alpha confidence interval for the selected quantiles of the data, with Maritz-Jarrett estimators.
    :param prob:
    :param alpha:
    :param axis:
    :return:
    """
    if len(data) < 2:
        return -1
    
    if variance(data) == 0.0:
        return 0.0
    
    alpha = min(alpha, 1 - alpha)
    z = norm.ppf(1 - alpha/2.)
    xq = hdquantiles(data, prob, axis=axis)
    med = round(xq[0], 5)
    if med == 0:
        return 0.0

    smj = 0.0

    try:
        smj = mjci(data, prob, axis=axis)
    except:
        return 0.0

    ci_bounds = (xq - z * smj, xq + z * smj)
    ci_lower = ci_bounds[0][0]
    ci_lower = 0 if ci_lower < 0 else ci_lower
    ci_upper = ci_bounds[1][0]
    ci_upper = 0 if ci_upper < 0 else ci_upper

    rciw = ((ci_upper - ci_lower) / med) * 100
    
    return rciw

def create_bench_dict(path):
    """
    read results-c1-.... file and creates a dictionary of a project. keys are benchmarks, values are execution times.
    :param path:
    :return:
    """
    benchdict = {}
    with open(path, 'r') as project_results_file:
        project_results = csv.reader(project_results_file, delimiter=';')
        for row in project_results:
            benchmark_name = row[2]
            if benchmark_name not in benchdict:
                benchdict[benchmark_name] = [float(row[3])]
            else:
                benchdict[benchmark_name].append(float(row[3]))
    return benchdict

def create_rciw_dict(command_result):
    splitted_result = command_result.split('\n')
    width_dict = {}
    for row in splitted_result:
        if not row.startswith('#') and row != '':
            splitted_row = row.split(';')
            key = "{0}_{1}".format(splitted_row[0], splitted_row[6])
            u = float(splitted_row[5])
            l = float(splitted_row[4])
            m = float(splitted_row[3])
            rciw = -1 if m == 0 else (u - l) / m
            width_dict[key] = (rciw, m, l, u)
    return width_dict

def create_bench_dict_pa(path):
    benchdict = {}
    with open(path, 'r') as project_results_file:
        project_results_file.readline()     # get rid of the title
        project_results = csv.reader(project_results_file, delimiter=';')
        for row in project_results:
            benchmark_name = row[2]
            if benchmark_name not in benchdict:
                benchdict[benchmark_name] = [float(row[11])]
            else:
                benchdict[benchmark_name].append(float(row[11]))
    return benchdict
