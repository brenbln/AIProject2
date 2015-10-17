__author__ = 'brenbln'

from constants import *
from helper import *

class Node:
    weight_1 = 1
    weight_2 = 1
    loc = ''
    name = ''
    total_processes = 0
    false_positives = 0
    false_negatives = 0
    true_positives = 0
    true_negatives = 0

    def __init__(self, name):
        self.name = name

    def handle_weight(self, x, y, loc):
        x = x/90 # Normalize the data
        y = y/180
        total = self.weight_1 * x + self.weight_2 * y
        if self.name == loc:
            expected = 1
        else:
            expected = 0
        if total > t_hold:
            outcome = 1
        else:
            outcome = 0
        self.weight_1 = self.weight_1 + learning_rate * (expected - outcome) * x
        self.weight_2 = self.weight_2 + learning_rate * (expected - outcome) * y
        # print self.weight_1, self.weight_2, expected, outcome, self.name
