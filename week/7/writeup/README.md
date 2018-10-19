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

Because we are supposed to be reverse engineering a binary file, it seemed like the best choice would be to open up the file in cutter, since it was one of the applications we discussed during the Binaries-II lecture. After opening up the file in cutter, I noticed this interesting block of code while scrolling through the file.   
```
|           0x00000790      mov  byte [local_13h], 0x74 ; 't'
|           0x00000794      mov  byte [local_12h], 0x6d ; 'm'
|           0x00000798      mov  byte [local_11h], 0x70 ; 'p'
|           0x0000079c      mov  byte [local_10h], 0x2f ; '/'
|           0x000007a0      mov  byte [local_fh], 0x2e ; '.'
|           0x000007a4      mov  byte [local_eh], 0x73 ; 's'
|           0x000007a8      mov  byte [local_dh], 0x74 ; 't'
|           0x000007ac      mov  byte [local_ch], 0x65 ; 'e'
|           0x000007b0      mov  byte [local_bh], 0x67 ; 'g'
|           0x000007b4      mov  byte [local_ah], 0x6f ; 'o'
```
From this, it looks like these lines of code are referencing something at the location `tmp/.stego`. I decided to execute the binary file by typing `./binary` in terminal, then went to the tmp directory to see what appeared. I tried using `cat` and `strings` on the file, but didn't see anything that resembled a flag.

I then executed `file .stego` to see if I could get information about the file (like in part 1), but only got `.stego: data`, which wasn't very helpful. I then tried using binwalk, which returned the following description `JPEG image data, JFIF standard 1.01`. I wasn't sure what a JFIF was, so I did some researching and found that *Valid JFIF files begin with FF D8 FF E0 ?? ?? 'J' 'F' 'I' 'F' 00* from [this](http://fileformats.archiveteam.org/wiki/JFIF) website. Given that information, I thought it would be a good idea to open up the file in a hex editor and noticed that there was an extra 00 at the beginning. After removing this I saved the file and was able to open it up and saw that it was a picture of a stegosaurus.

After seeing the type of dino, it seemed like this was a hint to use steganography to extract a flag from the image. So, I used the `steghide extract` command. When it prompted me for a password, I tried a few different things including steganography, dinosaur, and cmsc. Then, I tried stegosaurus, which resulted in a new file being created which gave me the flag **CMSC389R-{dropping_files_is_fun}**
