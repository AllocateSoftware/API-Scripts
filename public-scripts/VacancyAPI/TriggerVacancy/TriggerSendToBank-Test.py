import time
import sys

from stomp import *

import stomp

#Need to use auto_content_length=False otherwise stomp adds content-length header to message
#ActiveMQ uses existance of content-length to determine message type
#https://activemq.apache.org/stomp

AMQ_USER = input("Enter the user for AMQ? ")
AMQ_PASSWORD = input("Enter the password for AMQ? ")

conn = stomp.Connection([('interop-amq-dev.allocate-dev.co.uk', 61614)], auto_content_length=False)
conn.set_ssl([('interop-amq-dev.allocate-dev.co.uk', 61614)])

conn.set_listener('', PrintingListener())
conn.start()
conn.connect(AMQ_USER, AMQ_PASSWORD, wait=True)


#Load the dummy xml msg
with open('TempStaffEvent.xml') as xml_file:  
    event = xml_file.read()

conn.send('/topic/HR.TempStaff', event)

conn.disconnect()
