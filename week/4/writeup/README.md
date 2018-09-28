Writeup 3 - Pentesting I
======

Name: Ben Eisner
Section: Section 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ben Eismer

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag for this section of the assignment is `CMSC389R-{p1ng_as_a_$erv1c3}`. The first thing I did to find this flag was investigate the `nc cornerstoneairlines.co 45` command that was given in the readme. Executing this commnand in terminal brought you to a network administration panel that allows you to monitor the website uptime.

I tried typing in several IP addresses including both the cornerstoneairlines ip address as well as the admin server IP address. Unfortunately, entering these IP addresses into the prompt didn't reveal any flags. I thought it would be a good idea to research past vulnerabilities with ping in linux, since the server is running Ubuntu (This was found in a previous writeup). After doing a google search, I found this [website](https://www.netsparker.com/blog/web-security/command-injection-vulnerability/) which shows a past command injection vulnerability. One of the examples on the website looked like `127.0.0.1; id`, which gave me the idea to try something similar on the cornerstoneairlines. I tried typing in `127.0.0.1; echo "hello"` to see if I would be able to actually execute the command.

Executing this command ended up printing "hello" in the terminal which indicated that I was on the right track. However, in addition to the "hello" a lot of actual ping data was included as well. To try to fix this, I decided to just enter `;echo hello` into the uptime monitor and that ended up working. The next step now was to try to find the flag.

From some of the past exercises, I knew that executing `ls` is usually a good thing to do when interacting with a linux server. So, I typed in `;ls` into the uptime monitor. This ended up listing all of the directories. I wanted to see what was in the home directory, so I executed `;ls /home/`. After executing this, I saw that there was a file named `flag.txt` in the directory. So, I went on to enter `;cat /home/flag.txt`, which resulted in the flag being printed out.

Fred could do several things to fix this issue. First, he could password protect the interface. By doing this, a user wouldn't be able to gain access to the uptime monitor unless a correct password was entered. He could also disable semicolons from being entered. This would make the command injection no longer work. Third, he could disable the uptime monitor overall and use some external software that could be more secure. Finally, he could update the software on the server to patch this vulnerability.

### Part 2 (55 pts)

For this part of the assignment, we were required to create a program that would mimic an interactive shell on the server. Unlike a previous exercise where we had to crack a password to login, there was no login necessary here. From Part 1, I knew that we would have to use the ping vulnerability in this part somehow. I realized that I could just send the `nc cornerstoneairlines.co 45` command through the socket then send `;[command]` to allow any command to be entered and processed by the server.

To get started, I made a while loop that continuously asks the user for a command. After each command, the execute_cmd method was called, which creates a new socket and processes the entered command through the ping vulnerability. After I did this, I noticed that it would print out the "Cornerstone Airlines" text after every command I typed, which I didn't want. To fix this issue, I decided to insert an extra read into the socket which would get rid of the beginning part which we don't want to save. Now, the result from the executed command would be saved and returned by the execute_cmd method.

The one thing that I still had to figure out was how I would be able to cd, since we have to be able to handle going into a directory and up a level with this program. I realized I could add a cd to the line that would be sent in the socket. Now it would look like `;cd [location]; [command]`. To handle being able to go up one directory, I just saved the previous location to another variable and the made that the current location if `cd ..` was entered. We didn't have to handle invalid directories so I decided not to implement a great deal of invalid file/directory checking. I then created a while loop since you should only be able to enter in any shell command you want if you enter `shell` into the program. In addition to shell, I had to make some way to pull files from the remote host.

It seemed like the best way that I could do this would be to just add cat to the beginning of the command that would be sent in the socket. This would allow for the contents of a text file to be returned from the remote host. I then created a new text file with the given name and location, then copied the contents over to that file and saved it.

Finally, I just had to print help instructions if `help` was entered. This didn't involve anything more than calling a method that prints out the help instructions if `help` is entered. I also made `quit` the condition that would break the while loop, which would then exit the program.

To run the program, simply type in `python shell.py` and an interactive prompt will appear. Typing in `shell` will allow you to interact with the cornerstoneirlines.co server. Typing `pull` will allow you to pull files from the server. Typing `help` will show additional help instructions, and typing `quit`, will quit the program completely.
