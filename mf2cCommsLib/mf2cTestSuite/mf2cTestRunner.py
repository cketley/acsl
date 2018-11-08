'''
Created on 16 Oct 2017

@author: cheney
'''


import unittest
import os, sys
import subprocess
from stgdIngestFunctionals import StgDIngestFunct
from config import configObject
from ConfigParser import NoSectionError
import _threading_local
import threading



############################################################################

def DifficultTestingSuite():

    difficultTestSuite = unittest.TestSuite()
    difficultTestSuite.addTest(unittest.makeSuite(StgDIngestTestingFunctionals))
    return difficultTestSuite




###################################################


def Adhoc01TestingSuite():

    adhoc01TestSuite = unittest.TestSuite()


############################################################################



def ShortTestingSuite():

    shortTestSuite = unittest.TestSuite()

    shortTestSuite.addTest(StgDIngestTestingFunctionals("test_41313105_good_data_6recs_capture_reconciliation"))


#####################################################


def ComfortableLargeTestingSuite():

    comfortableLargeTestSuite = unittest.TestSuite()


    comfortableLargeTestSuite.addTest(StgDIngestTestingFunctionals("test_00000010_network_accessible"))
    comfortableLargeTestSuite.addTest(StgDIngestTestingFunctionals("test_00000020_python_available"))





myDifficultTestingSuite = DifficultTestingSuite()
myShortTestingSuite = ShortTestingSuite()
myComfortableLargeTestingSuite = ComfortableLargeTestingSuite()
myAdhoc01TestingSuite = Adhoc01TestingSuite()




if __name__ == '__main__':
    if "--short" in sys.argv:
        unittest.TextTestRunner(verbosity=2).run(myShortTestingSuite)
    elif "--difficult" in sys.argv:
        unittest.TextTestRunner(verbosity=2).run(myDifficultTestingSuite)
    elif "--comfortable" in sys.argv:
        unittest.TextTestRunner(verbosity=2).run(myComfortableLargeTestingSuite)
    elif "--adhoc01" in sys.argv:
        unittest.TextTestRunner(verbosity=2).run(myAdhoc01TestingSuite)
    else:
        pass
