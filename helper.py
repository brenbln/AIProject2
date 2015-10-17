__author__ = 'bbelen'

import sys
from constants import *

def read_data_file(filename):
    try:
        file = open(filename, 'r')
    except IOError:
        print 'ERROR, unable to open file. Check filename.'
        return 0
    else:
        datalist = []
        for line in file:
            # Replace this by putting each line into a list
            data = line.split()
            data[0] = float(data[0])
            data[1] = float(data[1])
            if len(data) > 3:
                data[3] = int(data[3])
            datalist.append(data)
    file.close()
    return datalist

def write_learned_weights(w1, w2, name):
    try:
        file = open(LEARNED_DATA, 'ab')
    except IOError:
        sys.exit('ERROR, unable to write file.')
    else:
        file.write(str(w1))
        file.write(' ')
        file.write(str(w2))
        file.write(' ')
        file.write(name)
        file.write(' ')
        file.write('\n')
    file.close()