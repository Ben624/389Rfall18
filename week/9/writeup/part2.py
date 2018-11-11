#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port =  7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
while True:
    data = s.recv(1024)
    print(data)
    match = re.search(r'Find me the (\w+) hash of (\w+)', data)

    if not match:
        print("Regex no longer matches. Exiting program...")
        break

    hash, target = match.groups()
    guess = getattr(hashlib, hash)(target).hexdigest()
    s.send(guess + '\n')

# close the connection
s.close()
