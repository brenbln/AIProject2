__author__ = 'bbelen'

from helper import *
from constants import *
from node import Node

# Runs the input data through the newly built neural network
def test(node, x, y, loc, num_fired):
    total = node.weight_1 * x + node.weight_2 * y
    if node.name == loc:
        expected = 1
    else:
        expected = 0
    if total > t_hold:
        outcome = 1
    else:
        outcome = 0

    if outcome == 0 and expected == 0:
        node.true_negatives += 1
        node.total_processes += 1

    elif outcome == 1 and expected == 1:
        node.true_positives += 1
        node.total_processes += 1
        num_fired += 1

    elif outcome == 0 and expected == 1:
        node.false_negatives += 1
        node.total_processes += 1

    elif outcome == 1 and expected == 0:
        node.false_positives += 1
        node.total_processes += 1
        num_fired += 1

    return num_fired

def compute_node_stats(node):
    true_positive_percent = float(node.true_positives)/float(node.total_processes)
    true_negative_percent = float(node.true_negatives)/float(node.total_processes)
    false_positive_percent = float(node.false_positives)/float(node.total_processes)
    false_negative_percent = float(node.false_negatives)/float(node.total_processes)

    print 'Neuron:', node.name
    print ' Correct:', str(round((true_positive_percent + true_negative_percent)*100,2)) + '%'
    print ' True Positives:', str(round((true_positive_percent*100),2)) + '%'
    print ' True Negatives:', str(round((true_negative_percent*100),2)) + '%'
    print ' False Positives:', str(round((false_positive_percent*100),2)) + '%'
    print ' False Negatives:', str(round((false_negative_percent*100),2)) + '%'

def compute_data_stats():
    print '\n'
    print 'Test Data Statistics:'
    print ' Total amount of data tested: ', len(test_datalist)
    print ' Correct number of neurons fired: ', correct_neuron_fired
    print ' Number of times zero neurons fired: ', zero_neuron_fired
    print ' Number of times multiple neurons fired: ', multiple_neuron_fired
    print '\n'
    print 'Test Data Statistics (Rounded Percentages):'
    print ' Correct number of neurons fired: ', str(
        round(float(correct_neuron_fired) / len(test_datalist) * 100, 2)) + '%'
    print ' Number of times zero neurons fired: ', str(
        round(float(zero_neuron_fired) / len(test_datalist) * 100, 2)) + '%'
    print ' Number of times multiple neurons fired: ', str(
        round(float(multiple_neuron_fired) / len(test_datalist) * 100, 2)) + '%'

N = []
process_count = 0
correct_neuron_fired = 0
zero_neuron_fired = 0
multiple_neuron_fired = 0
num_fired = 0

N.append(Node('Africa')) # 0
N.append(Node('America')) # 1
N.append(Node('Antarctica')) # 2
N.append(Node('Asia')) # 3
N.append(Node('Australia')) # 4
N.append(Node('Europe')) # 5
N.append(Node('Arctic')) # 6
N.append(Node('Atlantic')) # 7
N.append(Node('Indian')) # 8
N.append(Node('Pacific')) # 9

datalist = read_data_file(FILENAME)
open(LEARNED_DATA, 'w').close # This will wipe the file with the modified weights every time the program runs
for data in datalist:
    for node in N:
        node.handle_weight(data[0], data[1], data[2])

for node in N:
    write_learned_weights(node.weight_1, node.weight_2, node.name)

test_datalist = read_data_file(TEST_DATA)
for data in test_datalist:
    num_fired = 0
    for node in N:
        num_fired = test(node, data[0], data[1], data[2], num_fired)
    if num_fired == 1:
        correct_neuron_fired += 1
    elif num_fired == 0:
        zero_neuron_fired += 1
    elif num_fired > 1:
        multiple_neuron_fired += 1

# Compute statistics for each neuron
for node in N:
    compute_node_stats(node)

compute_data_stats()


