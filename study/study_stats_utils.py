from bisect import bisect_left
import itertools

import pandas as pd
import numpy as np
from scipy import stats

import itertools



def check_all_identical(arrays):
    """
    We define a function to check if all the given groups have identical values, which means we do not even have to run a statistical test.
    """

    return all([np.array_equal(x, y) for x, y in itertools.combinations(arrays, 2)])


def multiple_groups_test_dataframe(dataframe, group_1, group_2, metrics, testfunc, check_identical=True):
    """
    We define a function that builds a dataframe with the statistical tests results, based on two levels of grouping.
    """
    
    group_1 = group_1 if isinstance(group_1, (tuple, list)) else [group_1]

    # Create the result dataframe.
    test_df = pd.DataFrame(columns=group_1 + ['metric', 'pvalue'])

    # For each of the groups defined by "group_1", execute the test between samples defined by "group_2", for each of the metrics.
    for name, group in dataframe.groupby(group_1):
        name = name if isinstance(name, (tuple, list)) else [name]

        for metric in metrics:
            # Extract the samples.
            samples = [_group[metric].values for _name, _group in group.groupby(group_2) if len(_group) > 0]

            # Check if all the observations are equal between groups.
            if check_identical and check_all_identical(samples):
                pvalue = 1.0
            else:
                # Apply the test function to the groups.
                _, pvalue = testfunc(*samples)
            # Store the result.
            test_df = test_df.append({
                **{key: value for key, value in zip(group_1, name)},
                **{'metric': metric, 'pvalue': pvalue}
            }, ignore_index=True)
    
    # Return the dataframe.
    return test_df


def pairwise_multiple_groups_posthoc_test_dataframe(dataframe, group_1, group_2, metrics, testfunc):
    """
    We define a function that build a dataframe with the statistical pairwise tests results, based on two levels of grouping.
    """

    group_1 = group_1 if isinstance(group_1, (tuple, list)) else [group_1]

    # Create the result dataframe.
    test_df = pd.DataFrame(columns=group_1 + ['metric'] + [group_2] + ['comparison', 'pvalue'])

    # For each of the groups defined by "group_1", execute the pairwise test between samples defined by "group_2", for each of the metrics.
    for name, group in dataframe.groupby(group_1):
        # Exclude empty groups.
        if len(group) == 0:
            continue

        name = name if isinstance(name, (tuple, list)) else [name]

        d_1 = {key: value for key, value in zip(group_1, name)}
        
        for metric in metrics:
            d_2 = {'metric': metric}

            # Get the pairwise matrix of p-values.
            pvalues = testfunc(group, val_col=metric, group_col=group_2)
            
            # Transform the matrix dataframe into a long version.
            pvalues_long = pvalues.unstack().reset_index()
            pvalues_long.columns = ['first', 'second', 'value']
            
            # Put -1 on the diagonal.
            pvalues_long['value'] = np.where(pvalues_long['first'] == pvalues_long['second'], -1, pvalues_long['value'])

            # Store the result composing the row for the dataframe.
            for _, row in pvalues_long.iterrows():
                test_df = test_df.append({
                    **d_1,
                    **d_2,
                    **{group_2: row['first'], 'comparison': row['second'], 'pvalue': row['value']},
                }, ignore_index=True)

    # Return the dataframe.
    return test_df


def pairwise_multiple_groups_test_dataframe(dataframe, group_1, group_2, metrics, testfunc, check_identical=True):
    """
    We define a function that build a dataframe with the statistical pairwise tests results, based on two levels of grouping.
    """

    group_1 = group_1 if isinstance(group_1, (tuple, list)) else [group_1]

    # Create the result dataframe.
    test_df = pd.DataFrame(columns=group_1 + ['metric'] + [group_2] + ['comparison', 'pvalue'])

    # For each of the groups defined by "group_1", execute the pairwise test between samples defined by "group_2", for each of the metrics.
    for name, group in dataframe.groupby(group_1):
        # Exclude empty groups.
        if len(group) == 0:
            continue

        name = name if isinstance(name, (tuple, list)) else [name]

        d_1 = {key: value for key, value in zip(group_1, name)}
        
        for metric in metrics:
            d_2 = {'metric': metric}

            for x, y in itertools.product([(_name, _group[metric].values) for _name, _group in group.groupby(group_2) if len(_group) > 0], repeat=2):
                # Check if all the observations are equal between groups.
                if check_identical and check_all_identical([x[1], y[1]]):
                    pvalue = 1.0
                else:
                    # Apply the test function to the groups.
                    _, pvalue = testfunc(x[1], y[1])

                # Store the result composing the row for the dataframe.
                test_df = test_df.append({
                    **d_1,
                    **d_2,
                    **{group_2: x[0], 'comparison': y[0], 'pvalue': pvalue},
                }, ignore_index=True)

    # Return the dataframe.
    return test_df


def vargha_delaney(x, y):
    x = x.tolist() if isinstance(x, (pd.Series, np.ndarray)) else x
    y = y.tolist() if isinstance(y, (pd.Series, np.ndarray)) else y

    # Compute the size of the samples.
    n1, n2 = len(x), len(y)
    
    # Assign ranks to data.
    r = stats.rankdata(x + y)
    r1 = sum(r[0:n1])
    
    # Compute the effect size.
    a = (2 * r1 - n1 * (n1 + 1)) / (2 * n2 * n1)

    # Compute magnitude.
    levels = [0.147, 0.33, 0.474]
    magnitude = ['negligible', 'small', 'medium', 'large']
    scaled_a = (a - 0.5) * 2
    magnitude = magnitude[bisect_left(levels, abs(scaled_a))]
    
    # Return the results.
    return a, magnitude


def pairwise_multiple_groups_vda_dataframe(dataframe, group_1, group_2, metrics):
    group_1 = group_1 if isinstance(group_1, (tuple, list)) else [group_1]

    # Create the result dataframe.
    test_df = pd.DataFrame(columns=group_1 + ['metric'] + [group_2] + ['comparison', 'a', 'magnitude'])

    # For each of the groups defined by "group_1", execute the pairwise test between samples defined by "group_2", for each of the metrics.
    for name, group in dataframe.groupby(group_1):
        # Exclude empty groups.
        if len(group) == 0:
            continue

        name = name if isinstance(name, (tuple, list)) else [name]

        d_1 = {key: value for key, value in zip(group_1, name)}

        for metric in metrics:
            d_2 = {'metric': metric}

            for x, y in itertools.product([(_name, _group[metric].values) for _name, _group in group.groupby(group_2) if len(_group) > 0], repeat=2):
                a, magnitude = vargha_delaney(x[1], y[1])

                # Store the result composing the row for the dataframe.
                test_df = test_df.append({
                    **d_1,
                    **d_2,
                    **{group_2: x[0], 'comparison': y[0], 'a': a, 'magnitude': magnitude},
                }, ignore_index=True)

    # Return the dataframe.
    return test_df
