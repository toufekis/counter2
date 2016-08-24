#!/usr/bin/env python3
from sys import argv
import os
from multiprocessing import Pool

#script, pathname, tnumber = argv
script, pathname = argv

#k = ['\n', ' ', '#']
k = ['#']

def linecounter(filenames):
    count = 0
    f = open(filenames, 'r')
    for line in f.readlines():
        stripe = line.strip()
        count += 1
        if stripe == '' or stripe[0] in k:
            count -=1
    f.close()
    return count 

l = list()
lalala = 0
for roots, dirs, files in os.walk(pathname):
    
    if len(files) == 0:
        continue
    for specific in files:
        name = os.path.abspath(os.path.join(roots, specific))
        if not name.endswith('.py'):
            continue
        l.append(name)
        #lines = linecounter(name)
        #lalala += lines
#        print(name, lines, lalala)

#pool = Pool(int(tnumber))
pool = Pool()
k = pool.map(linecounter, l)
pool.close()
pool.join()
#print(lalala)
print(sum(k))
