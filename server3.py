import socket
import threading
import os
import getpass

def RetrFile(name, sock, sender):
    file_path = r"C:\\Users\\"+getpass.getuser()+"\\Documents\\"+sender+"_data"
    filename = sock.recv(1024)
    file_path = file_path + "\\" + str(filename) + ".zip"
    if os.path.isfile(file_path):
        sock.send("EXISTS " + str(os.path.getsize(file_path)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(file_path, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()

def Main(sender,ip):
    host = ip
    port = 5000
    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print "Server Started."
    c, addr = s.accept()
    print "client connected ip:<" + str(addr) + ">"
    RetrFile("RetrThread", c, sender)
    #while True:
    #    c, addr = s.accept()
    #    print "client connected ip:<" + str(addr) + ">"
    #    t = threading.Thread(target=RetrFile, args=("RetrThread", c, sender))
    #    t.start()
         
    s.close()

#Main('14103192','172.16.108.241')
