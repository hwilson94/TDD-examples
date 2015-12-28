# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:27:09 2015

@author: Harry
"""


def testMoneyMultiplication():
    """test multiplication for both Franc and Dollar at once"""
    Money = (Dollar, Franc)
    for currency in Money:
        assert currency(10) == FiveTimes(2)
        assert currency(15) == FiveTimes(3)


def Dollar(a):
    return a


def Franc(b):
    return b


def FiveTimes(c):
    return 5 * c
    