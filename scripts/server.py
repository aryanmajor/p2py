import socket
import threading
import socketserver
from .scripts import sendRequest

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        msg=data
        self.request.sendall("2:".encode('utf-8'))
        data.decode().split(":") #error
        print(data)
        if len(data)==5:
            if int(data[0])==0:
                #request received
                #check and forward
                if self.server.userdata['identity']==data[2]:
                    print('Someone wants your identity {}'.format(data[1]))
                    print('Requested at {}'.format(data[3]))
                reqThread=threading.Thread(target=sendRequest,args=(self.server.ippool,self.server.ownip,msg,))
                reqThread.start()
                reqThread.join()
            elif data[0]==1:
                #reply received
                #notify user
                if self.server.userdata['identity']==data[2]:
                    print('Someone approved your request {}'.format(data[1]))
                    print('Requested at {}'.format(data[3]))



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def openServer(ownip,ippool,uinfo):
    PORT =3010

    server = ThreadedTCPServer((ownip, PORT), ThreadedTCPRequestHandler)
    server.userdata=uinfo
    server.info={"ownip":ownip,"ippool":ippool}
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    return server
