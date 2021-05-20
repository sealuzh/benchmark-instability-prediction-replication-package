# This python file is intended to execute pa with separate projects' benchmarks' results and write each projects:
# name, benchmark, executions, mean, cv, RCIW1, RCIW2
# into a csv file called final.csv

# mean-cv --> -1 : only 1 datapoint for that benchmark    --> eliminate
#      cv --> 0.0 : all the points are the same           --> can be, is ok
# RCIW1, RCIW2 --> -1 : mean was 0
#                   0 : width was 0 but mean wasn't


import subprocess, calculation, csv, sys, os, tempfile

# path to pa tool binary
pa_path = sys.argv[1]
# run with 5, 10, 20, 30
nr_iterations = int(sys.argv[2])

iterations = [nr_iterations]

def main():
    final_file_name = "final_{}_iterations.csv".format(nr_iterations)
    final_file = open(final_file_name, 'w', newline='\n')
    final_file_writer = csv.writer(final_file, delimiter=',')
    pa_inputs_file = open('pa_input_projects.csv', 'r', encoding='utf-8', newline='\n')
    counter = 0
    for line in pa_inputs_file:
        counter += 1
        project_name = get_project_name(line)
        print("#{0} {1}".format(counter, project_name))
        file_path = os.path.join(os.getcwd(), *line.replace('\n', '').split('/'))
        # Benchmarkname --> datapoints
        data_points = calculation.create_bench_dict_pa(file_path)

        for it in iterations:
            # create temporary file for pa tool
            tf = tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', newline='\n', prefix='smb-vars-')
            tfn = tf.name
            # write datapoints up to the number of iterations
            write_iterations(tf, data_points, it)
            # Benchmarkname --> datapoints
            new_data_points = calculation.create_bench_dict_pa(tfn)
            # run pa tool
            args = [pa_path, '-sl', '0.05,0.01', '-bs', '10000', '-os', tfn]
            results = subprocess.check_output(args).decode('utf-8')
            # close and therefore delete temporary file
            tf.close()
            # Benchmarkname --> rciw
            rciw = calculation.create_rciw_dict(results)
            # write rciw values to CSV file
            write_out(final_file_writer, project_name, new_data_points, rciw, it)
        
    final_file.close()

def write_iterations(temp_file, data_points, iterations):
    tfw = csv.writer(temp_file, delimiter=';')
    tfw.writerow(['project', 'commit', 'benchmark', 'params', 'instance', 'trial', 'fork', 'iteration', 'mode', 'unit', 'value_count', 'value'])

    for key in data_points:
        dps = data_points[key]
        lenDps = len(dps)
        if lenDps < iterations:
            print(" remove {0} with {1} data points".format(key, lenDps))
            continue
        t = 0
        while t < iterations:
            tfw.writerow(['', '', key,'', 0, t, 0, 0, '', '', 1, dps[t]])
            t += 1
    temp_file.flush()

def write_out(out_file_writer, project_name, data_points, rciw, iterations):
    for key in data_points:
        executions = len(data_points[key])
        if executions > 1:                         # Basically eliminating if only 1 data point and mean is 0 (all points are 0)
            b_CV = calculation.calculate_CV(data_points[key])
            # b_COQV = calculation.calculate_COQV(data_points[key])
            b_RMAD = calculation.calculate_RMAD(data_points[key], samples = iterations)
            b_RMAD_HD = calculation.calculate_RMAD_HD(data_points[key], samples = iterations)
            b_RCIW_HD_99 = calculation.calculate_RCIW_MJ_HD(data_points[key], alpha = 0.01)
            b_RCIW95, m, *rest = rciw["{0}_0.95".format(key)]
            if b_RCIW95 != -1:
                b_RCIW95 *= 100
            b_RCIW99, *rest = rciw["{0}_0.99".format(key)]
            if b_RCIW99 != -1:
                b_RCIW99 *= 100
            if b_RCIW95 == -1 or b_RCIW99 == -1:
                print(" remove {0} with RCIW95={1} and RCIW99={2} 0".format(key, b_RCIW95, b_RCIW99))
                continue
            out_file_writer.writerow([project_name, key, executions, m, b_CV, b_RCIW95, b_RCIW99, b_RCIW_HD_99, b_RMAD, b_RMAD_HD])



def get_project_name(line):
    tmp = line.split('/')
    tmp2 = tmp[1].split('_')
    tmp3 = tmp2[0].split('&')
    project_name = tmp3[1] + '/' + tmp3[2]
    return project_name

if __name__ == '__main__':
    main()