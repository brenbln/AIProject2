__author__ = 'bbelen'

import ConfigParser
import sys

# Constants and constant checks (MODIFY settings.cfg file)
config = ConfigParser.ConfigParser()
config.readfp(open(r'settings.cfg'))

FILENAME = config.get('Settings', 'FILENAME')



