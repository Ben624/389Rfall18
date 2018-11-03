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
3.

4.

5.

6.

7.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1.

2.

3.

4.

5.
