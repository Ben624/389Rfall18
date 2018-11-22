#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct
import time


HASH_LOW = 6
HASH_HIGH = 15
BITS = 64
#####################################
### STEP 0: Socket Stuff ###
#####################################

host = "142.93.118.186"
port =  1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)


#####################################
### STEP 1: Calculate forged hash ###
#####################################
message = 'CMSC389R Rocks!'
s.send('1\n')
data = s.recv(1024)
s.send(message + '\n')
data = s.recv(1024)
split_data = data.split()
legit = split_data[len(split_data)-1]

fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'Ha Ha Ha. This is Malicious!'

fake_md5.update(malicious)

fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

data = s.recv(1024)

for i in range(HASH_LOW, HASH_HIGH + 1):
    padding = '\x80'
    next_pad = ('\x00' * (BITS - len(message) - i - 9))
    padding += next_pad
    padding += struct.pack('<Q', ((i+len(message))*8))
    payload = message + padding + malicious
    s.send('2\n')
    s.recv(1024)
    s.send(fake_hash + '\n')
    s.recv(1024)
    print("Sent: %s" %(payload))
    s.send(payload + '\n')
    time.sleep(1)
    data = s.recv(1024)

    if 'Hello,' not in data:
        break

#############################
### STEP 3: Print Results ###
#############################

print("Data: %s\n"%data)
print("Legit: %s" % legit)
print("Fake: %s" % fake_hash)
