Writeup 3 - OSINT II, OpSec and RE
======

Name: Ben Eisner
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ben Eisner

## Assignment 3 Writeup

### Part 1 (100 pts)

Mr. Krueger,

Hopefully you found the report regarding your website's vulnerabilities helpful, and I'm glad that you reached out to seek additional guidance.

The first major vulnerability I found was your website's open port (*1337*). This open port is what ultimately gave me access into your admin server which contained the flight records. In a fairly short period of time, the `nmap` tool was able to scan and identify all open ports. To fix this issue, I would first recommend checking your server settings for the open port. [This guide ](https://www.cyberciti.biz/faq/iptables-block-port/) discusses blocking ports on linux, which may be helpful in blocking the port. In addition, you could reach out to your website host and they could help with closing the port. Finally, you should make sure that your server has a firewall. [This webpage](https://www.ubuntupit.com/top-10-linux-firewall-software-for-protecting-your-linux-systems/) links to the Top 10 Linux firewall systems.

The second major issue I want to discuss is your username/password choice. The username to log into your admin server is `kruegster`, which is listed on multiple locations throughout your website like on the e-mail address which is shown on the about page as well as in the git repository. If other hackers attempt to hack into your server, they will immediately identify `kruegster` as useful information. Your admin password `pokemon` is also extremely unsafe. If hackers look at your Instagram account, they will immediately see all of your pokemon images, which could lead them to try 'pokemon' as the password. Additionally, the password is listed on several bruteforce password lists including `rockyou.txt`, which hackers commonly use. The first step to make sure your username and password are secure is to not post anything about those credentials online. If you didn't post that `kruegster` e-mail address and pokemon photos, it would have been a bit more difficult to figure out the login. Additionally, you should make sure that your password is secure. `pokemon` doesn't contain any capital letter, symbols, numbers, and is a word which makes it easy to guess. Many websites and services like `lastpass.com` can create strong passwords which are very hard for hackers to crack. Lastpass also allows you to store all of your password in one encrypted location. A website that you may find helpful is [Randomize.com](https://random-ize.com/how-long-to-hack-pass/). This site tells you the time it takes to crack a password. According to the site, `pokemon` takes 2 seconds to crack, while `G3sXnCk6g3NV!!`(a password generated from lastpass) would take over 506637647 years to crack. Just adding those few extra symbols can make a huge difference.

The final major vulnerability I wanted to address is regarding how easy it was to use bruteforce into your website. I was able to send several requests each second for hours at a time. To prevent these bruteforce attacks, you could set up your server to automatically deny access to a certain IP address after a certain number of attempts. Dreamhost, a popular web hosting platform allows [Extra web security](https://help.dreamhost.com/hc/en-us/articles/215947927-How-do-I-enable-Extra-Web-Security-for-my-website-), which will automatically detect bruteforce attacks and take the appropriate action. I would recommend speaking to your website host about implementing a feature similar to this. Additionally, some of the firewall services I mentioned in the first paragraph include features to prevent bruteforce attacks.

Hopefully you found this information helpful.
