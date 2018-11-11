Writeup 9 - Crypto I
=====

Name: *Ben Eisner*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ben Eisner*

## Assignment 9 Writeup

### Part 1 (60 Pts)
After reading the comments that were already included in stub.py, it seemed like the first thing I had to figure out was how to use `hashlib`. After looking at the module on the python documentation, I saw that there is a function `sha512()`. Considering the password is in SHA512, I knew this would be helpful.

After figuring out how to use `hashlib`, it was time to start coding. After seeing that the passwords come from a provided password list, I thought it would be a good idea to add a for loop that would go through all the passwords. So, I added `for word in wordlist:` before `for salt in salts:`.

Next, I stripped the word to remove any unwanted leading or trailing characters with `word = word.strip()`. Then, after looking back at the provided `hashlib` documentation, I used the sha512 function to get the desired hash with `hsh = hashlib.sha512(salt+word).hexdigest()`. I did `salt+word` instead of just word since in the Readme it says *'each password is salted by pre-pending a single, lowercase character'*.

Next, I just checked if `hsh`(from above) was included in the list of hashes provided in the hashes file. If hsh was in hashes, I printed out the the Salt and Password. After running the program, I got the following results:

```
Salt:m  Password:jordan
Salt:u  Password:loveyou
Salt:k  Password:neptune
Salt:p  Password:pizza
```



### Part 2 (40 Pts)
