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

Next, I stripped the word to remove any unwanted leading/trailing characters with `word = word.strip()`. Then, after looking back at the provided `hashlib` documentation, I used the sha512 function to get the desired hash with `hsh = hashlib.sha512(salt+word).hexdigest()`. I did `salt+word` instead of just word since in the Readme it says *'each password is salted by pre-pending a single, lowercase character'*.

Next, I just checked if `hsh`(from above) was included in the list of hashes provided in the hashes file. If hsh was in hashes, I printed out the the Salt and Password. After running the program, I got the following results:

```
Salt:m  Password:jordan
Salt:u  Password:loveyou
Salt:k  Password:neptune
Salt:p  Password:pizza
```



### Part 2 (40 Pts)

The first thing I decided to do with this part was plug in the given IP address and port into part2.py and run the program just to see what would happen. I got the following message:

```
=========================================
Hello there! Welcome to my hash workshop.
=========================================
Find me the sha384 hash of JGkJGWZjEj
```

After seeing this message and trying to enter several things into it, it seemed like this program was set up to continue asking for something like `Find me the [hash type] of [hash]` until you win the game. I thought the best way to handle this would be to use a regular expression. So, below the provided `s.connect` line, I added a `while True:` loop then moved `    data = s.recv(1024)` and `print(data)` into that loop.

After thinking about it, I decided that the best structure for the while loop is to match the received data with the regex, then break out of the loop and end the program if the regex doesn't match, since that would indicate you have won the game. To accomplish this, I added the following lines of code below the print statement.
```
match = re.search(r'Find me the (\w+) hash of (\w+)', data)

  if not match:
      print("Regex no longer matches. Exiting program...")
      break
```

If that loop didn't break, that would mean that the received data matched the regex, which means the game is still going. I decided to use the `groups()` and `getattr()` functions to generate a valid 'guess' that would be sent through the socket. The following lines accomplished this.

```
hash, target = match.groups()
guess = getattr(hashlib, hash)(target).hexdigest()
s.send(guess + '\n')
```

After finishing that, I ran the program and got the following output at the end: `You win! CMSC389R-{H4sh-5l!ngInG-h@sH3r}`.
