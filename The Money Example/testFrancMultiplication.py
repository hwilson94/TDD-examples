# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:27:09 2015

@author: Harry
"""


def testFrancMultiplication():
    """no explanation needed"""
    assert Franc(10) == FiveTimes(2)
    assert Franc(15) == FiveTimes(3)


def Franc(a):
    return a


def FiveTimes(b):
    return 5 * b
    