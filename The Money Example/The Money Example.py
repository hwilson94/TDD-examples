# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:27:09 2015

@author: Harry
"""


def testDollarMultiplication():
    """no explanation needed"""
    assert Dollar(10) == FiveTimes(2)
    assert Dollar(15) == FiveTimes(3)


def testFrancMultiplication():
    """no explanation needed"""
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
    DollarFive = 5
    DollarSix = 6
    FrancFive = 5
    FrancSix = 6
    assert DollarFive == DollarFive
    assert DollarFive != DollarSix
    assert FrancFive == FrancFive
    assert FrancFive != FrancSix


def Dollar(a):
    return a


def Franc(b):
    return b


def FiveTimes(c):
    return 5 * c



    