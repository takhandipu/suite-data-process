import read_perf_stat_csv as reader
import sys

def convert(folder_name,file_name):
    columns, data = reader.get_data(folder_name)
    out_file = open(file_name, 'w')
    print >>out_file, "Benchmark",
    for i in columns:
        print >>out_file, ",",i,
    print >>out_file, ""
    for key in data:
        print >>out_file, key,
        for i in columns:
            if i not in data[key]:
                data[key][i]=0.0
            print >>out_file, ",",data[key][i],
        print >>out_file, ""
    out_file.close()

convert(sys.argv[1],sys.argv[2])
