import socket

s=socket.socket()
s.connect(('',6969))

recv_pub = str(s.recv(1024).decode('utf-8')).split("DELIM",2)
print(recv_pub)
#pub []= recv_pub.split('DELIM')
plain = 13
cipher = pow(plain,int(recv_pub[0]),int(recv_pub[1]))
s.send(str(cipher).encode())

s.close()

