#! /usr/bin/env python3
#use to rename file, pre and post check

import os

os.chdir(r'C:\Users\Documents\Target folder')

for f in os.listdir(): # look for all files in this directory
    with open(f) as hostname: # open each files
          for line in hostname: 
                if "show version" in line: # read files for specific string
                      ff_hostname, ff_show = line.split('#') # split the output to two
##                      print(ff_hostname)
                
    f_ip, f_ext = f.split(' ') #split the original file to two
    ##print(f_ext)
    new_name = '{}{}'.format(ff_hostname,f_ext) # formats with a goal filename
    os.rename(f,new_name) # rename the file
