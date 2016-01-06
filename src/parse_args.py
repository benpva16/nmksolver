# parse_args.py
# Author: benpva16
# Date Created: 2016-01-05
# Purpose: parses command line arguments and return filename of board to use 

import sys

from print_help import print_help

def parse_args():
    if len(sys.argv) < 3:
        print("Too few arguments provided")
        print_help()
        return (0, 0)
    if sys.argv[1] == "-help":
        print_help()
        return (0, 0)
    if len(sys.argv) > 3:
        print("Too many arguments provided")
        print_help()
        return (0, 0)
    else:
        return (sys.argv[1][1:], sys.argv[2][1:])