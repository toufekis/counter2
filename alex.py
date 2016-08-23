#!/usr/bin/env python3
from sys import argv
import os

script, pathname = argv

#k = ['\n', ' ', '#']
k = ['#']

def linecounter(filenames):
   #Counts the number of lines in the given file. 
    count = 0
    f = open(filenames, 'r')
    for line in f.readlines():
        stripe = line.strip()
        count += 1
        if stripe == '' or stripe[0] in k:
            count -=1
    f.close()
    return count 


lalala = 0
for roots, dirs, files in os.walk(pathname): # Paragei tuples me (cwd, containig dirs, files in cwd)
    
    if len(files) == 0:
        continue
    for specific in files:
        name = os.path.join(roots, specific)
        if not name.endswith('.py'):    # Bgazei apotelesma mono gia arxeia .py
            continue
        lines = linecounter(name)
        lalala += lines
#        print(name, lines, lalala)
print(lalala)
