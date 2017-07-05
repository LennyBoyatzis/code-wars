# ChainMap allows us to link multiple mappings together to form a single unit
# When we try accessing one of the keys
# The ChainMap will go through each map in order to see if the key exists
# (starting with the first map it recieves)
# It return the first value that it find that matches the key
# This is useful for having defaults

import argparse
import os
import pdb
from collections import ChainMap

def main():
    app_defaults = {'username': 'admin', 'password': 'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key:value for key, value in vars(args).items() if value}
    chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain['username'])

if __name__ == "__main__":
    main()




