import csv
import sys
import os

def normalize(dictionary, key):
    if key not in dictionary:
        print "ERROR: key not in dictionary"
        sys.exit(-1)
    value=dictionary[key]
    for k in dictionary:
        if k!=key:
            dictionary[k]=(dictionary[k]/value)
    return dictionary

def get_row_from_file(filename):
    return_result={}
    with open(filename) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            return_result[row[2]]=float(row[0])
    return normalize(return_result,"instructions")

def get_data(folder_name):
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(folder_name):
        file_list.extend(filenames)
    
    data = {}
    
    for file in file_list:
        data[os.path.splitext(file)[0]] =  get_row_from_file(folder_name+'/'+file)
    columns = {}
    for benchmark in data:
        for key in data[benchmark]:
            if key not in columns:
                columns[key]=1
    return sorted(columns.keys()),data

#print get_data(sys.argv[1])

