#coding=utf-8
# NB we need to declare the code format so we can use multinational characters


'''
Created on 16 Oct 2017

@author: cheney
'''
import unittest
import valideer
import base64
import time
import json
import sys
from zlib import adler32

from mf2cComms.channel.channel import Channel
from mf2cComms.channel.channel import QosType
from mf2cComms.channel.channel import GdprType
from mf2cComms.channel.channel import ProtocolType
from mf2cComms.channel.channel import SecurityType
from mf2cComms.channel.msg.message import Message


class Test(unittest.TestCase):


    def setUp(self):
        self.friendlyName = u'bobCórrego01'
        self.temporaryData = "Hello to Bob from Alice's Computer"
        self.b64payload = base64.b64encode(self.temporaryData)
        self.dictPayload = {
            unicode('snt') : unicode(str(int(time.time()))),
            unicode('sz') : unicode(len(self.temporaryData)),       # length of data before uuencode or zipping
            unicode('szu') : unicode(len(self.b64payload)),
            unicode('szc') : unicode(0),
            unicode('sze') : unicode(0), 
            unicode('cks') : unicode(adler32(self.temporaryData)),
            unicode('dat'): self.b64payload  # dont unicode this because it could be very large and anyway its in uuencode format
        }
        self.msg = "test_ValideerMsgSz - size is not negative"
        self.message = Message(self.friendlyName)
        


    def tearDown(self):
        message = None
        
        

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass



    def test_ValideerMsgHdrVar(self):
        pass

    def test_ValideerMsgDat(self):
        pass

    def test_ValideerMsgCks(self):
        pass

    def test_ValideerMsgSz(self):
        
        self.assertFalse(self.message.__sanitiseSent(self.dictPayload, self.friendlyName))

        return True

    def test_ValideerMsgSzu(self):
        pass

    def test_ValideerMsgSzc(self):
        pass

    def test_ValideerMsgSze(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValideerMsg']
    unittest.main()