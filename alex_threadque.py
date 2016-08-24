#!/usr/bin/env python3
from sys import argv
import os
from queue import Queue
from threading import Thread
import multiprocessing

script, pathname = argv

#k = ['\n', ' ', '#']
k = ['#']
j = []

def linecounter(q):         #FIXME
    count = 0               # wrong output. why?
    while True:

        f = open(q.get(), 'r')
        for line in f.readlines():
            stripe = line.strip()
            count += 1
            if stripe == '' or stripe[0] in k:
                count -=1
        f.close()
        q.task_done()
        j.append(count)  

q = Queue(maxsize=0)
cpus = multiprocessing.cpu_count()

l = list()


for roots, dirs, files in os.walk(pathname):
    
    if len(files) == 0:
        continue
    for specific in files:
        name = os.path.join(roots, specific)
        if not name.endswith('.py'): 
            continue
        #l.append(name)  # Do i really need it?
        q.put(name)
        #lines = linecounter(name)
        #lalala += lines
#        print(name, lines, lalala)
#print(lalala)
for i in range(cpus):
    worker = Thread(target=linecounter, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()
print(sum(j))
