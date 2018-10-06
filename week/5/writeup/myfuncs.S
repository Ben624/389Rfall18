section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
        mov r11, 0    ;using r11 as the 'int i' in the for loop. Set it to 0.
                      ;storing in r11 since it only needs to be temporary.
mem_loop:
        cmp r11, rdx  ;compare the value of r11 (int i) to rdx (int strl / length)
        jge mem_exit  ;break out of the for loop if past the length
        mov[rdi+r11],sil ;else copy char val to the address (rdi+r11) (string pointer address + i)
        inc r11          ;increase r11 (i)
        jmp mem_loop     ;run the loop again

mem_exit:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
        mov r11,0     ;using r11 as the 'int i' in the for loop. Set it to 0.
cpy_loop:
        cmp r11, rdx  ;compare the value of r11 (int i) to rdx (int strl / length)
        jge cpy_exit  ;break out of the for loop if past the length
        mov r8b, [rsi+r11]  ;Copy the value from current position (r11) in src (rsi) to r8b (temp pointer low bit)
        mov [rdi+r11], r8b  ;Copy the value from r8b to the dest pointer (rdi) at current position r11
        inc r11             ;increase r11
        jmp cpy_loop        ;run the loop again
cpy_exit:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
