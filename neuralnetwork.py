__author__ = 'bbelen'

from helper import *
from constants import *
from node import Node

N = []
N.append(Node('Africa'))
N.append(Node('America'))
N.append(Node('Antarctica'))
N.append(Node('Asia'))
N.append(Node('Australia'))
N.append(Node('Europe'))
N.append(Node('Arctic'))
N.append(Node('Atlantic'))
N.append(Node('Indian'))
N.append(Node('Pacific'))

datalist = read_data_file(FILENAME)
open(FILE_TO_WRITE, 'w').close
for data in datalist:
    for node in N:
        node.handle_weight(data[0], data[1], data[2])

new_datalist = read_data_file(FILE_TO_WRITE)
for data in new_datalist:
    print data