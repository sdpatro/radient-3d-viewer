__author__ = 'sdpatro'
from controllers import main
import sys

arg_list = sys.argv
if len(arg_list) >= 2:
    main.run(arg_list[1])
else:
    print "Error: please enter the port number."
