import mf2cGenericTransport

import logging
import time
import json
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random


__author__ = "Emma Tattershall & Callum Iddon"
__version__ = "1.3"
__email__ = "etat02@gmail.com, jens.jensen@stfc.ac.uk"
__status__ = "Pre-Alpha"

STATUS_CONNECTED = "C"
STATUS_DISCONNECTED_GRACE = "DG"
STATUS_DISCONNECTED_UNGRACE = "DU"
HUB = 'broker_services'

logging.basicConfig(level=logging.INFO)



if __name__ == "__main__":
    hostname = <name of your host machine>
    port = 1883
    smart_agent = SmartAgent(hostname, '0001')
    smart_agent.setup()
    oldtimestamp = int(timestamp())
    try:
        while True:
            # Believe me, if you don't introduce a delay, this program will 
            # happily take up 90% of your CPU...
            time.sleep(0.1)
            
            # Get the messages in the buffer and deal with ping requests
            messages, pingacks = smart_agent.loop()
            if messages != []:
                for message in messages:
                    print(message)
            
            # Send a message every 10 seconds
            if int(timestamp()) - oldtimestamp >= 10:
                smart_agent.send(['Cheney'], {'payload': "Hello from Emma's Computer"}, security=0, qos=2)
                oldtimestamp = int(timestamp())
    except Exception as e:
        raise e
    finally:
        # clean up
        smart_agent.clean_up()
