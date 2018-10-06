Writeup 5 - Binaries I
======

Name: Ben Eisner
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ben Eisner

## Assignment 5 Writeup

### Background

The first time I worked with assembly was back in CMSC216, Introduction to Computer Systems. In this class, we were taught some basics of assembly as well as some techniques to correctly convert C code into assembly. One of the key difference between assembly and other languages is that assembly is a low-level language. Assembly doesn't have any neat tricks like other languages do. Assembly primarily consists of moving and setting values in registers. Additionally, unlike other languages, it can be very hard to tell what is going on in assembly, which is why comments are especially important.  

### memset()

After looking at the provided C code for this function, I knew that the first thing that I had to do was make a 'for loop' in assembly. To get the for loop working in assembly, I first had to create the 'int i' variable which will incrememt with the for loop. To make this variable, I decided to use the `r11` register, since according to the provided slides is a temporary register, which is appropriate in this scenario. Writing `mov r11, 0` sets the register to 0 and is essentially the same as doing `int i = 0`.

After that, I had to create a loop function, which is a function that will continue to be called until the specific condition is false. In this case, the loop should break if `i < len`. So, the first thing that I had to do in the loop was check if `i < length`. Since the length is the third argument passed into the function, it will be in the `rdx` register. So, doing `cmp r11, rdx` will compare i/r11 with the length value. If r11 is greater than rdx, the loop should break, which happens in the following line `jge mem_exit`. `mem_exit` is a function that was addeed above `leave` and simply exits the program. If the program makes it past `jge mem_exit`, that means that it should set str[i] to val.  `mov[rdi+r11],sil` accomplishes this. One thing that did trip me up briefly was having to do `rdi+r11` instead of just `r11` since it needs to get the memory address location of rdi (the string) then add i to it to get the current character. After that line, all that's left is to increase i/r11 by 1 and jump back to the top of the function.

### strncpy()

memset and strncpy are fairly similar functions, and the only differece between them is that instead of `mov[rdi+r11],sil`, you have to do:
```
mov r8b, [rsi+r11]
mov [rdi+r11], r8b  
```

The first line in this statement is saving the value of the current character at the src string (rsi) to the r8b register. When writing the code, I originally had the value being saved to the `rcx` register, but that produced the incorrect output. I realized I only needed the lower bytes so I switched to using `r8b`. After it saves the value to `r8b`, it copies the value to the position in the dst string (rdi). The rest of the code is identical to memset, except the function names are different.

### Debugging

As already discussed, I faced two main problems when writing the program. The first was correctly figuring out how to get the current character in the string pointer. But after realizing that I could just do `rsi+r11` or something equivalent, the problem disappeared. The other problem that I faced was deciding what register to save the value to with strncpy. After plating around with a few combinations, I found that using r8b, or any other register that can get the lower bits (r9b) works.
