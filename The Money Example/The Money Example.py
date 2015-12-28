# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:27:09 2015

@author: Harry
"""


def testDollarMultiplication():
    """test multiplication for Dollar"""
    assert Dollar(10) == FiveTimes(2)
    assert Dollar(15) == FiveTimes(3)


def testFrancMultiplication():
    """test multiplication for Franc"""
    assert Franc(10) == FiveTimes(2)
    assert Franc(15) == FiveTimes(3)


def testMoneyMultiplication():
    """test multiplication for both Franc and Dollar at once"""
    Money = (Dollar, Franc)
    for currency in Money:
        assert currency(10) == FiveTimes(2)
        assert currency(15) == FiveTimes(3)


def testEquality():
    """testing whether the equality function works for different currencies"""
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)


def Dollar(a):
    return a


def Franc(b):
    return b


def FiveTimes(c):
    return 5 * c



    