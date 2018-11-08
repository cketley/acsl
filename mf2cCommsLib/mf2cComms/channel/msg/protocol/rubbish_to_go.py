'''
Created on 2 Oct 2017

@author: cheney
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''



    
    def do_install(self):
        print "In do_install"

    def parkStuffHere(self):
        
        
        # assuming module foo with method bar
        functions = {ProtocolType.PROTO_MQTT: client.send}

        mystring = myfoo
        if mystring in functions:
            functions[mystring]()
        
        
        # assuming module foo with method bar
        import foo
        result = getattr(foo, 'bar')()
        
        dictMethod = {'do_install': do_install}
        method_name = 'do_install' # set by the command line options
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(method_name)
        if not method:
            raise NotImplementedError("Method %s not implemented" % method_name)
        method()

#        methods = {'install': install}
#        method_name = 'install' # set by the command line options
#        if method_name in methods:
#            methods[method_name]() # + argument list of course
#        else:
#            raise Exception("Method %s not implemented" % method_name)
    
    tunnelGeneric = self.Protocol
    
    
class ProtocolMqtt(self.tunnelGeneric):
    
    def __init__(self, friendlyName):
        return True
    
    



class Mf2cTrDatastream():

    def __init__(self):
        '''
        Allocate an ID to this datastream and return it
        '''
        self.datastreamID = str(uuid.uuid4())
        
        self.dictDatastream = {}
        # build a dictionary of attributes
        self.dictDatastreamAttribs = {}
        self.dictDatastream['datastreamID'] = self.dictDatastreamAttribs
        
        return None
    
    
    def prepDatastream(self, circuitFriendlyName, circuitID):
        
        self.dictDatastreamAttribs['circuitName'] = circuitFriendlyName
        self.dictDatastreamAttribs['circuitID'] = circuitID
        self.dictDatastreamAttribs['controlChannelID'] = ''
        self.dictDatastreamAttribs['dataChannelID'] = ''
        self.dictDatastreamAttribs['messageID'] = ''

        self.makeDataChannel(circuitFriendlyName, self.dictDatastreamAttribs)
        self.makeControlChannel(circuitFriendlyName, self.dictDatastreamAttribs)
        
        # insert the list containing attributes into the dictionary using 
        self.dictDatastream['datastreamID'] = self.dictDatastreamAttribs        
        return True
        

    def sendGeneric(self, circuitFriendlyName, circuitID, hostName, destination, transportType, channelType, payload_dict, security, qos):
        
        self.prepDatastream(circuitFriendlyName, circuitID)
        self.messageID = str(uuid.uuid4())
        self.dictDatastreamAttribs['messageID'] = self.messageID

        self.destination = destination 
        self.hostName = hostName
        
        if channelType == 'data':
            ###self.openDataChannel(circuitFriendlyName, self.dictDatastreamAttribs)
            self.sendSpecificDataChannel(circuitFriendlyName, transportType, payload_dict, security, qos)
        elif channelType == 'control':
            ###self.openControlChannel(circuitFriendlyName, self.dictDatastreamAttribs)
            self.sendSpecificControlChannel(circuitFriendlyName, transportType, payload_dict, security, qos)
        else:
            ###self.openDataChannel(circuitFriendlyName, self.dictDatastreamAttribs)
            self.sendSpecificDataChannel(circuitFriendlyName, transportType, payload_dict, security, qos)
            
        return True
    
    
    
    
    def sendSpecificDataChannel(self, circuitFriendlyName, transportType, payload_dict, security, qos):
        if transportType == 'mqtt':
            self.actionMQTT(payload_dict, security, qos)
        elif transportType == 'http':
            self.actionHTTP(payload_dict, security, qos)
        elif transportType == 'btle':
            self.actionBluetoothLE(payload_dict, security, qos)
            
        return True

    
    def sendSpecificControlChannel(self, circuitFriendlyName, transportType, payload_dict, security, qos):
        if transportType == 'mqtt':
            self.actionMQTT(payload_dict, security, qos)
        elif transportType == 'http':
            self.actionHTTP(payload_dict, security, qos)
        elif transportType == 'btle':
            self.actionBluetoothLE(payload_dict, security, qos)
            
        return True

    
    
    
    def receiveGeneric(self, receiveID):
        
        
        ### manual poll or callback
        
        
        return True
    

    def receiveSpecific(self, receiveID):
        return True

        
        
        
    def makeDataChannel(self, circuitFriendlyName, dictDatastreamAttribs):
        dataChannelID = str(uuid.uuid4())
        self.dictDatastreamAttribs['dataChannel'] = dataChannelID
        
        return True
    
    def makeControlChannel(self, circuitFriendlyName, dictDatastreamAttribs):
        controlChannelID = str(uuid.uuid4())
        self.dictDatastreamAttribs['controlChannel'] = controlChannelID
        return True
    
    def openDataChannel(self, circuitFriendlyName, dataChannelID, dictDatastreamAttribs):
        self.dictDatastreamAttribs['dataChannel'] = dataChannelID        
        return True
    
    def openControlChannel(self, circuitFriendlyName, controlChannelID, dictDatastreamAttribs):
        self.dictDatastreamAttribs['controlChannel'] = controlChannelID
        return True
    
    def mightWork(self):


    
        