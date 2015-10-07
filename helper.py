__author__ = 'bbelen'

import sys

def read_data_file(filename):
    try:
        file = open(filename, 'r')
    except IOError:
        sys.exit('ERROR, unable to open file. Check filename.')
    else:
        datalist = []
        for line in file:
            # Replace this by putting each line into a list
            data = line.split()
            datalist.append(data)
    file.close()
    return datalist