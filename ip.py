import socket
host ='www.google.co.in'
try:
    addr=socket.gethostbyname(host)
    print('IP Address='+addr)
except socket.gaierror:
    print('The website does not exist:')