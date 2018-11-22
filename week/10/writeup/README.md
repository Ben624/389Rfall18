Writeup 10 - Crypto II
=====

Name: *Ben Eisner*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ben Eisner*

## Assignment 10 Writeup

### Part 1 (70 Pts)

For this part of the assignment, the first thing that I did was execute `nc 142.93.118.186 1234` so I could understand how the notary works. After I understood how it functions, I started to write the `stub.py` code. I thought that using sockets would be better than manually having to send *fake_hash* and *payload*, so I started by adding the standard socket code that has been given to us in previous assignments.

After that, I sent a *1* to select the first option in the notary followed by the message `CMSC389R Rocks!` since it was the message used in the example on the slides. Then, I then receivd the data, split it, and saved that as *legit*. I also made up a malicious string.

Next, I moved on to the *Craft Payload* section. After reviewing the slides, I figured figured out how to correctly craft the payload. I added the following lines in the second section (BITS = 64) (HASH_LOW = 6):

```
padding = '\x80'
next_pad = ('\x00' * (BITS - len(message) - i - 9))
padding += next_pad
padding += struct.pack('<Q', ((HASH_LOW + len(message))*8))
payload = message + padding + malicious
```

Following that, I sent a *2* since we want to use the notary's *Test a signature's validity* option. I then sent/received the provided *fake_hash* followed by the *payload* that was just created. I then received the data. I then surrounded the entire section in a loop that goes from *HASH_LOW*(6) to *HASH_HIGH*(15). I also changed *HASH_LOW* in the padding code to i so it would be different for each iteration in the loop. I also added the following code at the bottom of the loop:

```
if 'Hello,' not in data:
    break
```
If the received data does not contain *Hello,*, then it is different than the usual data that is returned, which means a flag was most likely found. After executing the program the following data was returned:

```
Now let me see...

Wow... I've never signed this data before!
This is crazy... I can't let anyone know that my service is broken!
Hey, if I give you this flag, you better keep quiet about this!
CMSC389R-{i_still_put_the_M_between_the_DV}
Made in Maryland - Substantial
```

```
Legit: 3e712579cf19ab4f68ea69ce2044c176
Fake: cc161d4805dd305bb564b5a310e3525a
Message: CMSC389R Rocks!
Malicious: Ha Ha Ha. This is Malicious!
Payload: CMSC389R Rocks!??Ha Ha Ha. This is Malicious!
```

Since we now have the flag `CMSC389R-{i_still_put_the_M_between_the_DV}`, we can move on to the next part of the assignment.


### Part 2 (30 Pts)

Since all of the PGP commands are provided to us in the slides, this part of the assignment was fairly straightforward. The first thing I did was `gpg --gen-key` to generate the key. I entered in my name and e-mail address followed. I entered `gpg --list-secret-keys` as well just to make sure the key was generated. Then I imported the provided public key by doing `gpg --import pgpassignment.key`.

Next, I created a message text file which will be encrypted. After creating the text file I executed `gpg -e -u "Ben Eisner" -r "UMD Cybersecurity Club" message.txt`. I got the following message after executing the command then typed *y*:
```
gpg: 37E0973B53D21CDC: There is no assurance this key belongs to the named user
sub  rsa2048/37E0973B53D21CDC 2018-11-09 UMD Cybersecurity Club <president@csec.umiacs.umd.edu>
 Primary key fingerprint: C140 F701 9C5F CF20 E12A  454F 9665 C74E 448C 470E
      Subkey fingerprint: 24E8 6295 0881 1D2A 7B8E  55FF 37E0 973B 53D2 1CDC

It is NOT certain that the key belongs to the person named
in the user ID.  If you *really* know what you are doing,
you may answer the next question with yes.

Use this key anyway? (y/N) y
```
This resulted in a new file *msg.txt.gpg* being generated. I finished the assignmeent by renaming the file to *message.private* and putting it in the writeup folder. 
