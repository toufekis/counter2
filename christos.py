#!/usr/bin/env python3
from sys import argv
import os
import fileinput
from multiprocessing.dummy import Pool as ThreadPool

script, pathname = argv

#k = ['\n', ' ', '#']
k = ['#']

pool = ThreadPool(2)

filelist = list()

for roots, dirs, files in os.walk(pathname):
    if len(files) == 0:
        continue
    for filename in files:
        name = os.path.abspath(os.path.join(roots, filename))
        if not name.endswith('.py'):
            continue
        filelist.append(name)

linesum = 0
for k in map(fileinput.input(), filelist):
    stripe = k.strip()
#for line in fileinput.input(files=filelist):
#    stripe = line.strip()

    #linesum += 1 if (stripe != '' or stripe[0] not in k) else 0

    if stripe == '' or stripe[0] in k:
        linesum += 0
    else:
        linesum += 1
print(linesum)
