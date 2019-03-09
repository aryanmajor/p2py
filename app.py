import sys

from scripts import scripts,clientui,server

# global variable
userdata={}
localip=''

if __name__=="__main__" :
    print("Initializing Application")
    localip=scripts.getlocalip()
    print("Connecting To Server....")
    try:
        IPpool=scripts.fetch_ip_pool(localip)
    except Exception as e:
        print('Error Occured')
        sys.exit(e)
    print("..Done")

    print("\nSetting Server\n")
    myserver=server.openServer(localip,IPpool)
    print("\nServer Set up")

    clientui.clientui(userdata,IPpool,localip)

    print(userdata)

    print("\nClosing Application")

    myserver.shutdown()
    myserver.server_close()

    print("\nBye\n")
