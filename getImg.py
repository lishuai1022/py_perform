#!/usr/bin/env python
#coding:utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
imgname = sys.argv[3]
pn95file = sys.argv[4]

def getMultiImg(xlist,ylist1,ylist2,filename):
    plt.title('img')
    plt.plot(xlist, ylist1, color='blue', label='before')
    plt.plot(xlist, ylist2, color='red', label='after')
    plt.legend() # 显示图例
    plt.xlabel('position')
    plt.ylabel('time')
    plt.savefig(filename)
    # plt.show()

def readList(name):
    res = []
    with open(name) as f:
        for line in f.readlines():
            res.append(float(line.rstrip('\n')))
    return res



def main():
    ylist1 = readList(file1)
    ylist2 = readList(file2)
    num = len(ylist1)
    xlist = xrange(1,num+1)
    getMultiImg(xlist,ylist1,ylist2,imgname)

    #pn95
    pn_title = ['次数','pn25','pn50','pn75','pn90','pn95','pn99']
    y1_25 = str(ylist1[int(num * 0.25)-1])
    y1_50 = str(ylist1[int(num * 0.5)-1])
    y1_75 = str(ylist1[int(num * 0.75)-1])
    y1_90 = str(ylist1[int(num * 0.90)-1])
    y1_95 = str(ylist1[int(num * 0.95)-1])
    y1_99 = str(ylist1[int(num * 0.99)-1])
    y1_pn_95 = [str(num),y1_25,y1_50,y1_75,y1_90,y1_95,y1_99]

    y2_25 = str(ylist2[int(num * 0.25)-1])
    y2_50 = str(ylist2[int(num * 0.5)-1])
    y2_75 = str(ylist2[int(num * 0.75)-1])
    y2_90 = str(ylist2[int(num * 0.90)-1])
    y2_95 = str(ylist2[int(num * 0.95)-1])
    y2_99 = str(ylist2[int(num * 0.99)-1])
    y2_pn_95 = [str(num),y2_25,y2_50,y2_75,y2_90,y2_95,y2_99]

    file = open(pn95file,'w')
    file.write('    '.join(pn_title))
    file.write('\n')
    file.write('    '.join(y1_pn_95))
    file.write('\n')
    file.write('    '.join(y2_pn_95))
    file.close()


if __name__ == '__main__':
    main()