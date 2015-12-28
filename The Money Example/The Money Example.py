# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:27:09 2015

@author: Harry
"""

Money = (Dollar, Franc)


def testDollarMultiplication():
    """test multiplication for Dollar"""
    assert Money[0](10) == FiveTimes(2)
    assert Money[0](15) == FiveTimes(3)


def testFrancMultiplication():
    """test multiplication for Franc"""
    assert Money[1](10) == FiveTimes(2)
    assert Money[1](15) == FiveTimes(3)


def testMoneyMultiplication():
    """test multiplication for both Franc and Dollar at once"""
    for currency in Money:
        assert currency(10) == FiveTimes(2)
        assert currency(15) == FiveTimes(3)


def testEquality():
    """testing whether the equality function works for different currencies"""
    assert Money[0](5) == Money[0](5)
    assert Money[0](5) != Money[0](6)
    assert Money[1](5) == Money[1](5)
    assert Money[1](5) != Money[1](6)
    assert Money[1](5) != Money[0](5)


def Dollar(a):
    return a


def Franc(b):
    return b


def FiveTimes(c):
    return 5 * c



    