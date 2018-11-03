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
1.

2.

3.

4.

5.
