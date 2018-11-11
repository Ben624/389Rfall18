
#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

# a set of the hashet split with the new line character
hashes = open('../hashes', 'r').read().split('\n')

for word in wordlist:
    for salt in salts:
    # do stuff
        word = word.strip()
        hsh = hashlib.sha512(salt+word).hexdigest()
        if(hsh in hashes):
            print 'Salt:%s  Password:%s' % (salt, word)
