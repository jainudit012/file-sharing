# Driver for sending file
import os
import datetime
import split
import getpass
watch = datetime.datetime.now()


def mainfunc(fuser,password,tuser,name,path):
    xyz = r"net use * /delete /y"
    path601 = r"C:\Users\\" + getpass.getuser() + "\\Documents\data_dump"
    subprocess.Popen(xyz, stdout=subprocess.PIPE, shell=True)
    # login as global admin
    cde = r"\\fileserver2.pdc.jiit\14103192 iphone5S+ /USER:14103192"
    p101 = subprocess.Popen(cde, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p101.communicate('dir c:\\')
    print stdout
    #subprocess.Popen(xyz, stdout=subprocess.PIPE, shell=True)
    parts = split.fsplit(path,path601)
    path = r"\\fileserver2\14103192\abcd\file_sending\\"+tuser
    if(not os.path.exists(path)):
        os.makedirs(path)
    path = path + "\\" + fuser + ".txt"
    fobj = open(path,"w")
    s = password + " " + name + " " + str(watch.day) + ":" + str(watch.month) + ":" + str(watch.year)
    fobj.write(s)
    fobj.close()
    path61 = r"\\fileserver2.pdc.jiit\14103192\abcd\dump_value\\"+tuser
    if not os.path.exists(path61):
        os.makedirs(path61)
        path62 = path61 + "\\parts"
        os.makedirs(path62)
    path63 = path61 + "\\info.txt"
    fobj = open(path63,"w")
    index = 1
    for i in range(parts):
        string =  
        
    
    
