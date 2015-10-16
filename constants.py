__author__ = 'bbelen'

import ConfigParser
import sys

# Constants and constant checks (MODIFY settings.cfg file)
# config = ConfigParser.ConfigParser()
# config.readfp(open(r'settings.cfg'))
#
# FILENAME = config.get('Settings', 'FILENAME')
FILENAME = 'nnTrainData.txt'
LEARNED_DATA = 'learneddata.txt'
TEST_DATA = 'nnTestData.txt'
learning_rate = 0.0000001
t_hold = 0.5



