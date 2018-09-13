Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Ben Eisner
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ben Eisner

## Assignment 2 writeup

### Part 1 (45 pts)

1. kruegster1990's real name is Fred Krueger. I found this from his [twitter](https://twitter.com/kruegster1990) profile.


2. The first thing I did was check the given username `kruegster1990` on `checkusernames.com`. Since this was the website given in class, it seemed like the best place to start. This site led me to his Twitter and Reddit pages. The reddit page didn't contain any information, however, the Twitter page was very helpful. In addition to giving his name, it also contained some personal information as well as a link to his [website](http://cornerstoneairlines.co). I also typed in his username into facebook, but didn't get any results. However, I did find his instagram page after doing a search for it on Instagram. Based on his Instagram images, it seems like he also has an interest for Pokemon.

  > **Twitter** https://twitter.com/kruegster1990 <br>
   **Reddit:** https://www.reddit.com/user/kruegster1990 <br>
   **Personal Info:** Born in 1990, From Silver Spring,MD <br>
   **Interests** Planes, Flying, Pokemon


3. To find the IP Address of the webserver, I did a reverse DNS lookup on `ultratools.com`. From this, I learned that the IP address of cornerstoneairlines.co is `142.93.118.186`.  

4. The first thing that I did when trying to find hidden files on the website was inspect the webpage with the inspect element tool built into chrome. In the home page code, I found the flag `CMSC389R-{h1dden_fl4g_in_s0urce}`. Then, I went to the robots.txt file as that was another point mentioned in class. In the text file I noticed `Disallow: /secret` which led me to navigate to that folder on the website, where I found another flag `CMSC389R-{fly_th3_sk1es_w1th_u5}`. After that, I ran ran two URL fuzzer tools (dirbuster and AngryFuzzer), and found the following directories.

| Type | Found           |
|------|-----------------|
| Dir  | /icons/         |
| Dir  | /.git/          |
| Dir  | /secret/        |
| Dir  | /server-status/ |
| Dir  | /.git/          |

After seeing the `/.git/` directory, I decided to go through the files inside. In the 'COMMIT_EDITMSG', I found the flag `CMSC389R-{y0u_found_th3_g1t_repo}`

5. In addition to the main IP address for the website, I noticed that the admin page had a seperate IP address, which is `142.93.117.193`. I found this because this address is what is in the URL when you navigate to the Admin page.

6. While looking for the location of the two servers, I encountered somewhat inconsistent data. According to `iplocation.net`, it seems like the servers are either in New Jersey, New York, or Ontario. The ISP for both servers is DigitalOcean, LLC.  

7. The server is running Apache/2.4.18 (Ubuntu). I found this information by typing in a bad link on the website and looking at the bottom line of the Not Found Webpage

8. In addition to the 3 flags already mentioned, I also found a flag while doing the DNS Lookup on `ultratools.com`. The flag is `CMSC389R-{dns-txt-rec0rd-ftw}`.

### Part 2 (55 pts)

After the lecture in class on Friday, it seemed like the first thing that I had to do was find some available ports that I would be able to hack. I decided to use nmap to find the open ports. Given that there was a seperate IP address for the admin page on the website, I decided to run nmap using that IP address. I was using Windows at the time so I used the nmap gui app. After running nmap with the ``intense scan, all TCP ports profile``, I got the following results.

| Port | Protocol |State     | Service   | Version           |
|------|----------|----------|-----------|-------------------|
| 80   | tcp      | Open     | http      |Apache httpd 2.4.18|
| 1337 | tcp      | Open     | waste     |N/A                |
| 2222 | tcp      | Open     | ssh       |OpenSSH7.2p2       |
|10010 | tcp      | Open     | rxapi     |N/A                |
| 11211| tcp      | Filtered | memcache  |N/A                |

From these results, I decided to first try to nc into the ssh port with the command ``nc 142.93.117.193 2222``. I didn't have any luck with this so I decided to try again with the 1337 port. That ended up working, and I was prompted with a username and password in terminal. This seemed like the place that I wanted to be, so I then went on to make the bruteforce program to figure out the password.

After playing around with the sockets in python, I got the program working to the point where a username and password could be sent, and the corresponding result was received to the result variable *(See Stub.py)*. I wasn't sure what would be returned if the result wasn't `Fail`, so I made the if statement check `if result != "Fail\n"` instead of something like `if result != "success\n"`. I then went on to implement the program being able to read `rockyou.txt` and loop through each password until the result wasn't `Fail`.

Since Fred's username for several of his accounts was `kruegster1990`, I thought that would be the username for the admin login. I inputted that username into the program and let it run. After several hours of it working, I was starting to think that it was the wrong username, but just to be safe, I decided to let it run overnight. After not seeing the program still run into the morning, I decided to stop the program and try to find another possible login.

One of the things that was mentioned in class was that people tend to leave traces of important information on sites like github or pastebin. Since I had already found the `/.git/` folder, I thought it would be a good place to look. I found that in `/logs/HEAD`, there was an e-mail address kruegster@tutanota.com . Later on realized that this e-mail address was also in the about section on the website. After seeing this e-mail address, I decided to try running the bruteforce program again, but with `kruegster` as the username. This time around, in just a few minutes, I was able to get the password `pokemon`. This password wasn't really a huge surprise thinking back to his Instagram page.

All that was left was finding the flight record on the system. Since I now had the username, password, IP, and port, gaining access to a terminal was accomplished just by entering `nc 142.93.117.193 1337`. After I logged in, it looked like I was in a linux shell. Executing `ls` seemed like a good way to start so I could see the files and directories. It looked like a fairly standard linux system, so I thought checking the home directory would be a good idea. Upon cd'ing into the home directory, I saw that there was a `flight_records` folder which contained many text files. At first, I was originally thinking of making another bruteforce program that would open each text file and check each line for `CMSC`, which would indicate a flag. However, I then remembered that among all of Fred's pokemon pictures on Instagram, there were three pictures in a row which resembled a ticket. On the second ticket image, there was the code `AAC27670`. Upon looking back in the flight records files, I saw that there was a file named `AAC27670.txt`. I tried to open the file with vim, but nothing happened, so I just typed in `cat AAC27670.txt`instead and received the flag `CMSC389R-{c0rn3rstone-air-27670}`. I went through several more directories in the terminal, but didn't find any additional flags. 
