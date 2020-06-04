import urllib.request
import socket

ip = urllib.request.urlopen('http://inet-ip.info/ip').read().decode('utf-8')

url = 'http://'+ ip + '/hi/'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read()
