#!/usr/bin/python
#coding = utf-8


def rigdeRegression(xMat, yMat, lam = 0.2):
    xTx = xMat.T*xMat
    denmon = xTx + eye(shape(xMat)[1]) * lam
    if linalg,det(demon) == 0.0 :
        print "the matrix is singular"
        return
    ws = denom.T * (xMat.T * yMat)
    return ws

