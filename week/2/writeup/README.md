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

*REPLACE THIS TEXT WITH A BRIEF EXPLANATION OF YOUR APPROACH TO SOLVING THIS CHALLENGE, AND THE OUTCOME*
