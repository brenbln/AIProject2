__author__ = 'brenbln'

from constants import *

class Node:
    weight_1 = 1
    weight_2 = 1
    loc = ''

    def __init__(self, name):
        self.name = name

    def handle_weight(self, x, y, loc):
        total = self.weight_1 * x + self.weight_2 * y
        if self.name == loc:
            expected = 1
            print('Got here', self.name, loc)
        else:
            expected = 0

        if total > t_hold:
            outcome = 1
        else:
            outcome = 0
        while outcome != expected:
            self.weight_1 = self.weight_1 + learning_rate * (expected - outcome) * x
            self.weight_2 = self.weight_2 + learning_rate * (expected - outcome) * y
            total = self.weight_1 + self.weight_2
            if total > t_hold:
                outcome = 1
            else:
                outcome = 0
        print self.weight_1, self.weight_2