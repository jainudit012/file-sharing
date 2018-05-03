import sys, os
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(100 * megabytes)
def fsplit(fromfile, todir, chunksize=chunksize): 
    if not os.path.exists(todir):                  # caller handles errors
        os.mkdir(todir)                            # make dir, read/write parts
    else:
        for fname in os.listdir(todir):            # delete any existing files
            os.remove(os.path.join(todir, fname)) 
    partnum = 0
    input = open(fromfile, 'rb')                   # use binary mode on Windows
    while 1:                                       # eof=empty string from read
        chunk = input.read(chunksize)              # get next part <= chunksize
        if not chunk: break
        partnum  = partnum+1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj  = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()                            # or simply open(  ).write(  )
    input.close(  )
    assert partnum <= 9999                         # join sort fails if 5 digits
    return partnum
#fsplit(r"C:\Users\Ekansh\Desktop\test\ralink_wireless_pcie_drv_500460000_win.zip",r"C:\Users\Ekansh\Desktop\test\vid")
