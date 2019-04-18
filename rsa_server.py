import socket
from keygen import keygen
pub_key,pri_key,N = keygen()
s=socket.socket()
s.bind(('',6969))
s.listen(1)


try:
	while True:
		conn,addr=s.accept()
		pubKey=str(pub_key)+"DELIM"+str(N)
		conn.send(str(pubKey).encode())		
		
		#receving
		cipher = int(str(conn.recv(1024).decode("utf-8")))
		print("received measage ",cipher)
		plain = pow(cipher,pri_key,N)
		print("Decrypted message : ",plain)


except KeyboardInterrupt:
	s.close()

