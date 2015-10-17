__author__ = 'bbelen'

from helper import *
from constants import *
from node import Node

# Runs the input data through the newly built neural network
def test(node, x, y, loc, num_fired):
    x = x/90 # Normalize the data
    y = y/180
    total = node.weight_1 * x + node.weight_2 * y
    if node.name == loc:
        expected = 1
    else:
        expected = 0
    if total > t_hold:
        outcome = 1
    else:
        outcome = 0
    # print node.name, node.weight_1, node.weight_2, expected, outcome

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
    print ' Total amount of data tested: ', correct_neuron_fired + zero_neuron_fired + multiple_neuron_fired
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
    print '\n'

def auto_train_test():
    global node, test_datalist, num_fired
    global correct_neuron_fired
    global zero_neuron_fired
    global multiple_neuron_fired
    global learning_rate
    datalist = read_data_file(FILENAME)
    open(LEARNED_DATA, 'w').close  # This will wipe the file with the modified weights every time the program runs
    for i in range(0, num_epochs):
        for data in datalist:
            for node in N:
                node.handle_weight(data[0], data[1], data[2])
        learning_rate *= 0.8  # Decrements the learning rate, thanks to Lucas and Rex for this idea
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

N = []
process_count = 0
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
choice = 0
correct_neuron_fired = 0
zero_neuron_fired = 0
multiple_neuron_fired = 0

open(LEARNED_DATA, 'w').close

#--------------------------------- Menu
while (choice != 7):
    print '1) Run training and testing automatically'
    print '2) Perform training'
    print '3) Store current weights into file'
    print '4) Initialize weights with file or automatically'
    print '5) Display weights'
    print '6) Perform testing and display statistics'
    print '7) Exit'
    choice = input('Select an option (enter the number): ')

    if choice == 1:
        auto_train_test()

    elif choice == 2:
        training_file = raw_input('Enter a valid file name: ')
        datalist = read_data_file(training_file)
        if datalist != 0 and len(datalist) > 0:
            for i in range(0, num_epochs):
                for data in datalist:
                    for node in N:
                        node.handle_weight(data[0], data[1], data[2])
                learning_rate *= 0.8  # Decrements the learning rate, thanks to Lucas and Rex for this idea (as well as normalizing the values

    elif choice == 3:
        open(LEARNED_DATA, 'w').close
        for node in N:
            write_learned_weights(node.weight_1, node.weight_2, node.name)

    elif choice == 4:
        initialize_choice = input('1) Initialize all weights to 1\n2) Load input weights\nEnter choice: ')
        if initialize_choice == 1:
            for node in N:
                node.weight_1 = 1
                node.weight_2 = 1
        elif initialize_choice == 2:
            datalist = read_data_file(LEARNED_DATA)
            for data in datalist:
                for node in N:
                    if data[2] == node.name:
                        node.weight_1 = data[0]
                        node.weight_2 = data[1]

    elif choice == 5:
        for node in N:
            print node.weight_1, node.weight_2, node.name

    elif choice == 6:
        testing_file = raw_input('Enter a valid file name: ')
        test_datalist = read_data_file(testing_file)
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

    elif choice == 7:
        sys.exit()


