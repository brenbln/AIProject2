__author__ = 'bbelen'

import helper
import constants
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

datalist = helper.read_data_file(constants.FILENAME)
for data in datalist:
    for node in N:
        node.handle_weight(data[0], data[1], data[2])
