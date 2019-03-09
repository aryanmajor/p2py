import socket
import json
import requests

def getlocalip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def fetch_ip_pool(ownip):
    reply=requests.get('http://192.168.21.217:3000/'+ownip)
    return json.loads(reply.text)['ip']

def sendRequest(ippool,ownip,msg):
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    i=0
    # send request to all the IP pool
    while i<len(ippool):
        ip=ippool[i]
        c.connect((ip,3010))
        c.send(msg.encode('utf-8'))
        msg=c.recv(1024)
    c.close()
    pass
