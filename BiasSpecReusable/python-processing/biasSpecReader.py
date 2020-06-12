#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue March 06, 2018

@author: Biplav Srivastava (biplavs@us.ibm.com)
"""

import json

# --------------------------------------------------------------
# Load utility
def loadJSON(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

# --------------------------------------------------------------
# Load bias spec and process
if __name__ == '__main__':

    specs = loadJSON('../data/input/biasTestParameters.json')

    # Uncomment below line for just dumping specs
    #print specs

    # We will just print name of bias spec
    i = 1
    for spec in specs:
        print "spec " + i.__str__() + ": "
        print spec["name"]
        i = i + 1
