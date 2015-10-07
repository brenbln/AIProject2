__author__ = 'bbelen'

import helper
import constants

datalist = helper.read_data_file(constants.FILENAME)
for data in datalist:
    print data

