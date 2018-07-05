#!/usr/bin/env python
#coding:utf-8

import  requests
import sys
import hashlib

url = sys.argv[1]
num = int(sys.argv[2])
filename = sys.argv[3]


def getTotalSeconds(url):
    response = requests.get(url)
    return response.elapsed.total_seconds()

def getResList(url,num):
    res = []
    for i in xrange(1,num+1):
        time = round(getTotalSeconds(url),3)
        res.append(str(time))
        res.sort()
    return res
    
def writeList(name,list_data):
    file=open(name,'w')  
    file.write('\n'.join(list_data))
    file.close() 

def main():
    ylist = getResList(url,num)
    writeList(filename,ylist)

if __name__ == '__main__':
    main()