from .scripts import sendRequest
import time

def clientui(userdata,ippool,ownip):
    print('Enter Your Name: ')
    userdata["name"]=input()
    print('Enter Your Identifier (a/b/c/d): ')
    userdata["identity"]=input()
    while True:
        print('1. Send Request\n0. exit')
        x=int(input())

        if x==1:
            print("Enter Indentifier (a/b/c/d): ")
            id=input()
            msg="0:"+ownip+":"+id+":"+str(time.time())+":"+str(10)
            sendRequest(ippool,ownip,msg)
        elif x==0:
            break
    pass
