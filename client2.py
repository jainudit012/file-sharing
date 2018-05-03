import socket

def Main(ip,filename):
    host = ip
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    #filename = raw_input("Filename? -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open(filename+'.zip', 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"

    s.close()
    
#Main('172.16.108.241','spartacus')
