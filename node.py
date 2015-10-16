__author__ = 'brenbln'

from constants import *
from helper import *

class Node:
    weight_1 = 1
    weight_2 = 1
    loc = ''

    def __init__(self, name):
        self.name = name

    def handle_weight(self, x, y, loc):
        total = self.weight_1 * x + self.weight_2 * y
        print self.weight_1
        print self.weight_2
        if self.name == loc:
            expected = 1
            print 'Got here, must match', self.name, loc
        else:
            expected = 0
        print self.name, 'Expected:', expected
        if total > t_hold:
            outcome = 1
        else:
            outcome = 0
        print self.name, 'Outcome:', outcome
        while outcome != expected:
            print self.name, 'Modifying weight'
            self.weight_1 = self.weight_1 + learning_rate * (expected - outcome) * x
            self.weight_2 = self.weight_2 + learning_rate * (expected - outcome) * y
            total = self.weight_1 + self.weight_2
            print 'Total', total
            print 'Threshold', t_hold
            if total > t_hold:
                outcome = 1
            else:
                outcome = 0
        write_network(round(self.weight_1,5), round(self.weight_2, 5), self.name, outcome)
        print self.weight_1, self.weight_2, expected, outcome