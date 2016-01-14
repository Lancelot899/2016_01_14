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


def locally_weighted_linear_regression(point, dataSet, labels, k = 1.0):
    m = shape(dataSet)[0]
    weights = mat(eye(m))
    for i in xrange(m):
        diffMat = point - dataSet[j, :]
        weights[j, j] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = dataSet.T * weights * dataSet
    if linalg.dat(xTx) == 0.0:
        print "This matrix is singular"
        return
    ws = xTx.I * (dataSet.T * weights * labels)
    return ws

if __name__ == '__main__':
    dataSet, labels = loadDataSet("./3D_spatial_network")
    point = mat([42995123, 8.536732456, 58.34534555])
    print locally_weighted_linear_regression(point, dataSet, labels)
