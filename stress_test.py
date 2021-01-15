# Created By Sukarna Jana

import psutil
from time import ctime
import time
from math import sin, cos, radians
import csv

count = 0
Myfile = open("data.csv",'a')
printData = csv.writer(Myfile)
iTime = 0
fTime = 0

def bench():
    start = time.time()
    product = 1.0
    for counter in range(1, 1000, 1):
        for dex in list(range(1, 360, 1)):
            angle = radians(dex)
            product *= sin(angle)**2 + cos(angle)**2
    end = time.time()
    return end - start

iTime = time.time()
printData.writerow(["Date-Time","hexadecimal","CPU %","Benchmark time","Running From"])
while True:
    try:
        print(hex(count))
        count += 1
        hexdata = hex(count)
        power = bench()
        fTime = time.time()
        printData.writerow([ctime(),hexdata,psutil.cpu_percent(),power,fTime - iTime])
    except KeyboardInterrupt:
        break
        
Myfile.close()
