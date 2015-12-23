import socket
import sys
import BaseHTTPServer
import httplib
import threading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webserveraddr = socket.gethostbyname(socket.gethostname())
server_address = (webserveraddr, 8282)
sock.bind(server_address)
sock.listen(1)

webserver = []
port = 8822

for i in range(5):
	webserver.append('http://192.168.1.5:8581')
for i in range (3):
	webserver.append('http://192.168.1.5:8582')
for i in range (3):
	webserver.append('http://192.168.1.5:8583')
for i in range (3):
	webserver.append('http://192.168.1.5:8584')
for i in range (3):
	webserver.append('http://192.168.1.5:8585')
	
print >>sys.stderr, 'starting up on %s port %s' % server_address
#conn = httplib.HTTPConnection

global ip
ip=0
while True:
	connection, client_address = sock.accept()
	data = connection.recv(2048)
	#print data
	direktori = data.split()
	try :
		#web_path = 'http://192.168.1.5:8582'
		respon ="\HTTP/1.1 302 Found\r\nLocation: %s" %webserver[ip]
		ip=ip+1
		if (ip == len(webserver)):
			ip=0
		#Location: 
		print respon
			#test.send_response(302)
			#test.send_header('Location', web_path)
			#test.end_headers()
		connection.send(respon)
	except :
		respon = "\HTTP/1.1 200 OK \n\ngambar tidak ada"
		connection.send(respon)
	
	connection.close()