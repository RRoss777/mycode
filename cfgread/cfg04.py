#!/usr/bin/env python3

import os

new_name= print(input("What would you like to name this file?")

# Renaming the file
os.rename(cfg04.cfg, new_name)
        
## create file object in "r"ead mode
with open(new_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

confignum = len(configlist)
print('Total lines:', confignum)
