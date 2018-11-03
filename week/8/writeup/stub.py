#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import struct


# You can use this method to exit on failure conditions.

def bork(msg):
    sys.exit(msg)


def get_type(type):
    if type == SECTION_PNG:
        return 'PNG'
    elif type == SECTION_DWORDS:
        return 'DWORDS'
    elif type == SECTION_UTF8:
        return 'UTF8'
    elif type == SECTION_DOUBLES:
        return 'DOUBLES'
    elif type == SECTION_WORDS:
        return 'WORDS'
    elif type == SECTION_COORD:
        return 'COORDS'
    elif type == SECTION_REFERENCE:
        return 'REFERENCE'
    elif type == SECTION_ASCII:
        return 'ASCII'
    else:
        return 'ERROR'


# Some constants. You shouldn't need to change these.

MAGIC = 0xdeadbeef
VERSION = 0x1

if len(sys.argv) < 0x2:
    sys.exit('Usage: python2 stub.py input_file.fpff')

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.

with open(sys.argv[0x1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

(magic, version, timestamp, author, section_count) = \
    struct.unpack('<LLL8sL', data[0:24])

if magic != MAGIC:
    bork('Bad magic! Got %s, expected %s' % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork('Bad version! Got %d, expected %d' % (int(version),
         int(VERSION)))

print '------- HEADER -------'
print 'MAGIC: %s' % hex(magic)
print 'VERSION: %d' % int(version)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

# Valid Section Types

SECTION_PNG = 0x1
SECTION_DWORDS = 0x2
SECTION_UTF8 = 0x3
SECTION_DOUBLES = 0x4
SECTION_WORDS = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_ASCII = 0x9

# Additional PNG Signature

PNG_HEX_SIG = (0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A,)
DATA_LENGTH = len(data)

# Offset
offset_start = 24

num_sections= 0

print '\n-------  BODY  -------'
print 'TIMESTAMP: %s' % int(timestamp)
print 'AUTHOR: %s' % (author)
print 'SECTIONCOUNT: %s' % int(section_count)

while offset_start < DATA_LENGTH:
    num_sections += 1
    offset_end = offset_start + 8
    (type, length) = struct.unpack('<LL', data[offset_start:offset_end])
    print '\nType:%s -- Count:%d' % (get_type(type), num_sections)

    # ********PNG********
    if type == SECTION_PNG:
        offset_start = offset_end
        offset_end += length
        out = PNG_HEX_SIG + struct.unpack('<%dB' % length, data[offset_start:offset_end])
        file = open('output.png', 'w')
        file.write(struct.pack('<%dB' % len(out), *out))
        file.close()
        print "PNG Saved to \'output.png\'"

    # ********DWORD********
    elif type == SECTION_DWORDS:
        num = length / 8
        result = []
        for x in range(0,num):
            offset_start = offset_end
            offset_end += 8
            result.append(struct.unpack('<Q', data[offset_start:offset_end])[0])
        print result

    # ********UTF8********
    elif type == SECTION_UTF8:
        num = length / 8
        result = []
        for x in range(0,num):
            offset_start = offset_end
            offset_end += 8
            result.append(struct.unpack('<Q', data[offset_start:offset_end])[0])
        print result

    # ********DOUBLES********
    elif type == SECTION_DOUBLES:
        num = length / 8
        result = []
        for x in range(0,num):
            offset_start = offset_end
            offset_end += 8
            result.append(struct.unpack('<Q', data[offset_start:offset_end])[0])
        print result

    # ********WORDS********
    elif type == SECTION_WORDS:
        num = length / 4
        result = []
        for x in range(0,num):
            offset_start = offset_end
            offset_end += 4
            result.append(struct.unpack('<L', data[offset_start:offset_end])[0])
        print result

    # ********COORD********
    elif type == SECTION_COORD:
        offset_start = offset_end
        offset_end += 8
        result = []
        #First coordinate
        result.append(struct.unpack('<d', data[offset_start:offset_end])[0])
        offset_start = offset_end
        offset_end += 8
        #Second coordinate
        result.append(struct.unpack('<d', data[offset_start:offset_end])[0])
        print result

    # ********REFERENCE********
    elif type == SECTION_REFERENCE:
        num = length / 4
        result = []
        for x in range(0,num):
            offset_start = offset_end
            offset_end += 4
            result.append(struct.unpack('<L', data[offset_start:offset_end])[0])
        print result

    # ********ASCII********
    elif type == SECTION_ASCII:
        offset_start = offset_end
        offset_end += length
        print (struct.unpack('<%ds' % length, data[offset_start:offset_end])[0])

    # ********INVALID********
    else:
        bork('Invalid Section Type')
    offset_start = offset_end
