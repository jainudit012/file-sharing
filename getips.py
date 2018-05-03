import socket
import netifaces

def get_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipv4 = s.getsockname()[0]
    s.close()
    return ipv4
def get_mask():
    gws = netifaces.gateways()
    return gws['default'][netifaces.AF_INET][0]

def getinfo():
    return {'ipv4':str(get_ipv4()),'default_gateway':str(get_mask())}

#print getinfo()
