Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Ben Eisner
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ben Eisner

## Assignment 8 Writeup

### Part 1 (45 Pts)

1. Yes, the traceroute command was used on any website. After loading the pcap file into wireshark, I used the *icmp* filter to figure out if traceroute has been used. Upon looking at the results, I noticed that the destination for all of the results was `142.93.118.186`, which would indicate that traceroute was being used on that address. After putting that address into the web browser I noticed that it's the IP address for Cornerstone Airlines.

2. After looking at the hint given in the slides, it seemed like the best thing to do first would be to analyze the TCP stream. I highlighted a random line but noticed that TCP stream was grayed out. I kept on going through the lines until the option became available for me to select. The TCP stream resulted in what appeared to be a chat transcript, which is copied below.
From this chat transcript, it looks like the hackers used the name **laz0rh4x** and **c0uchpot4doz**.


```
please enter a username: c0uchpot4doz
c0uchpot4doz, you are now in the chat room

<laz0rh4x> hey man, are you there?
yeah. when is it happening?

<laz0rh4x> we're all set for tomorrow at 1500

<laz0rh4x> did you get the updated plans?
no, can you send them over?

<laz0rh4x> https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

<laz0rh4x> done. you can read that with the parser I gave you last week
thanks, see you tomorrow

<laz0rh4x> good luck, don't be late
```  
3. After I closed out of the TCP Follow Window, I noticed that the filter `tcp.stream eq 2` was inputted. It looks like this filter contains all of the contents of the chat between the hackers. After looking at the source column, I noticed that there are two IP address used to send attacks to Cornerstone Airlines. These two IP addresses are *206.189.113.189* and *142.93.118.186*. After getting these IP's I decided to use IPlocation.net to get the location of these two addresses. *206.189.113.189* is located in **London, England** and *142.93.118.186* is located in **New Jersey**.

4. From the Info section of the list from the *tcp.stream eq 2*, I saw that the two ports being used are 2749 and 53878.

5. Yes, from the chat it seems like these two hackers are discussing some updated plans, which would indicate that some plans were changed for some unknown reason. My guess is that they are planning out a plan to hack Cornerstone Airlines. Also according to their message chain, it will take place *tomorrow at 1500* which is 3pm.

6. Yes, they did send a link `https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing` in the chat window. This file has a .fpff extension which after doing a google search appears to be the Forensics Playground File Format.


7. From the chat message chain, the two hackers are planning on meeting eachother tomorrow at 1500.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. With the `struct.unpack` function, I received a timestamp with the value **1540428007**. I then found a Epoch converter online and copied the number. This resulted in the timestamp `Thursday, October 25, 2018 12:40:07 AM`.

2. With the `struct.unpack` function, I found that the author is `laz0rh4x`.

3. According to the result from `struct.unpack`, there are 9 sections. However, after counting up all sections that were printed in the body section of the stub.py program, it appears that there are actually 11 sections.

4.

*Type:ASCII -- Section:1*:
 `Call this number to get your flag: (422) 537 - 79461`

*Type:WORDS -- Section:2*:
 `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]`

*Type:COORDS -- Section:3*:
`[38.99161, -77.02754]`

*Type:REFERENCE -- Section:4*:
`[1]`

*Type:ASCII -- Section:5*:
`The imfamous security pr0s at CMSC389R will never find this!`

*Type:ASCII -- Section:6*:
`The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}`

*Type:COORDS -- Section:7*:
`[38.9910941, -76.9328019]`

*Type:PNG -- Section:8*:
![alt text](https://raw.githubusercontent.com/Ben624/389Rfall18/master/week/8/writeup/output.png "Output")

*Type:ASCII -- Section:9*:
`AF(saSAdf1AD)Snz**asd1`

*Type:ASCII -- Section:10*:
`Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9`

*Type:DWORDS -- Section:11*:
`[4, 8, 15, 16, 23, 42]`

5. The PNG image gives you the flag `CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}`. To get this valid PNG to save, I realized that the File Signature was missing. To fix this issue, I addded the signature `(0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A)` in front of the struct.unpack for the PNG image. 
