#!/usr/bin/env python3
from sys import argv
import os, fileinput

script, pathname = argv

k = ['#']

#mypath = '/home/my/Documents/projects/counter/'
#filename = 'bla.py'

def linecounter(filenames):
    count = 0
    for lines in fileinput.input(files=filenames):
        lines = lines.strip()
        count +=1
        if lines == '' or lines[0] in k:
            count -= 1
    return count

l = list()
for roots, dirs, files in os.walk(pathname):
    #l += files 
    if len(files) == 0:
        continue
    for specific in files:
        name = os.path.join(roots, specific)
        if not name.endswith('.py'):
            continue
        l.append(name)

x = linecounter(l)
print(x)
