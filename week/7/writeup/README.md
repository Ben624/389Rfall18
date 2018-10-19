Writeup 7 - Forensics I
======

Name: Ben Eisner
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ben Eisner

## Assignment 7 writeup

### Part 1 (40 pts)

1. The file is a JPEG. I found this by running `exiftool image` and looking at the *File Type* section.

2. The GPS Position of the photo is *41° 53' 54.87" N , 87° 37' 22.53" W*. After plugging this information into Google Maps, I found that this photo was taken at the **John Hancock Center in Chicago, Illinois 60611**.

3. The photo was taken at the timestamp **2018:08:22 11:33:24**. I found this by running `exiftool image` and looking at the *Created Date* section.

4. The photo was taken on an **iPhone 8 back camera 3.99mm f/1.8**. I found this by running `exiftool image` and looking at the *Lens Model* section.

5. The photo was taken **539.5 m Above Sea Level**. I found this by running `exiftool image` and looking at the *GPS Altitude* section.

6. After looking at the Forensics 1 Slides, I decided to first try using the *strings* command to look for a flag. I executed `strings image | grep "CMSC"` in terminal and got the flag **CMSC389R-{look_I_f0und_a_str1ng}**. After that, I thought I may be able to find another flag by using *binwalk*, From the slides, I tried doing `binwalk image` and `binwalk -e image` but didn't get any flags. Then, I tried `binwalk --dd="png:png" image` and saw that it created a new directory (*_image.extracted*). After looking in this directory, I saw a PNG image which once opened, revealed another flag **CMSC389R-{abr@cadabra}**

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*
