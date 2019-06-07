import socket
import sys
import socks
import socket


# Socks5_host = "39.98.224.87"
# Socks5_port = 1080

Socks5_host = "114.233.50.176"
Socks5_port = 17478




# socks.setdefaultproxy(socks.SOCKS5, Socks5_host, 1080)
# socket.socket = socks.socksocket

# # for test udp, but don't work
# # Magic!
# def getaddrinfo(*args):
#     return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
# socket.getaddrinfo = getaddrinfo

# import urllib
# from urllib import request

# response = request.urlopen(r'http://www.baidu.com/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
# page = response.read()
# page = page.decode('utf-8')
# print(page)


HOST, PORT = "39.98.224.87", 9999
data = "1231"

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
sock.set_proxy(socks.SOCKS5, Socks5_host, Socks5_port)

try:
# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
except Exception as e:
    print(e)

received = str(sock.recv(1024), "utf-8")
print("Sent:     {}".format(data))
print("Received: {}".format(received))