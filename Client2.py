import socket
host='local host'
port=5000
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind((host,port))
msg,addr=s.recvfrom(1024)

try:
    s.settimeout(5)
    while msg:
        print("REcieved:"+msg.decode())
        msg,addr=s.recvfrom(1024)
except socket.timeout:
    print("Time is over and hence terminating:")

s.close()