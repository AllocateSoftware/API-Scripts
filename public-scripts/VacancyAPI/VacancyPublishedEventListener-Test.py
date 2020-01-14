import time
import sys

from stomp import *

import stomp

AMQ_USER = input("Enter the user for AMQ? ")
AMQ_PASSWORD = input("Enter the password for AMQ? ")

conn = stomp.Connection([('interop-amq-dev.allocate-dev.co.uk', 61614)])
conn.set_ssl([('interop-amq-dev.allocate-dev.co.uk', 61614)])

conn.set_listener('', PrintingListener())
conn.start()
conn.connect(AMQ_USER, AMQ_PASSWORD, wait=True)

conn.subscribe(destination='/topic/pw.eventstream.topic.AllocateConnect.Events', id=1, ack='auto')

print ('Ready')

while 1:
  time.sleep(10)
  print ('Waiting')

conn.disconnect()