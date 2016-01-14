#!/usr/bin/python
#coding = utf-8

from numpy import *

def loadDataSet(fileName):
    fr = open(fileName)
    dataList = []
    labelList = []
    for line in fr.readlines():
        textline = line.split(',')
        lineLen = len(textline)
        dataline = []
        for i in xrange(lineLen):
            dataline.append(float(textline[i]))
        labelList.append(float(textline[-1]))
        dataList.append(dataline)
    dataSet = mat(dataList)
    labels = mat(labelList).transpose()
    return dataSet, labels

def lineRegres(dataSet, labels):
    w = (dataSet.T * dataSet).I * (dataSet.T * labels)
    return w

if __name__ == '__main__':
    dataSet, labels = loadDataSet('./3D_spatial_network')
    print lineRegres(dataSet, labels)
