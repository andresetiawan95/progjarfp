import sys,socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 8080)
sock.bind(server_address)
sock.listen(10)
print >>sys.stderr, 'starting up on %s port %s' % server_address
# Listen for incoming connections
while True:
    	# Wait for a connection
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
    	# while True:
        data = connection.recv(2048)
	#print data
	direktori = data.split()
	#print direktori
	dir1=direktori[1]
	if direktori[1][0]=='/' :
		try :
			fopen=open("capture.jpg","rb")
			gambar = fopen.read()
			respon ="\HTTP/1.1 200 OK \n\n%s"%gambar
			fopen.close()
		except :
			respon = "\HTTP/1.1 200 OK \n\ngambar tidak ada"
	#print direktori[1][1:]  	
	#respon = "Sukses Menyambung ke Web Server"
	
	connection.send(respon)
	# Clean up the connection
	connection.close()
