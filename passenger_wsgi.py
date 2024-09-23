import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

# point to your project wsgi.py file
wsgi = imp.load_source('wsgi', 'deployla/wsgi.py')

application = wsgi.application