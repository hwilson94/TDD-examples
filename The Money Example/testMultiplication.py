# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:27:09 2015

@author: Harry
"""


def testMultiplication():
    """no explanation needed"""
    assert Dollar(10) == FiveTimes(2)
    assert Dollar(15) == FiveTimes(3)


def Dollar(a):
    return a


def FiveTimes(b):
    return 5 * b
    