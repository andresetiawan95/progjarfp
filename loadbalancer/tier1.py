import sys
import socket
import SocketServer
import SimpleHTTPServer
tierhandler = SimpleHTTPServer.SimpleHTTPRequestHandler;
webserveraddr = socket.gethostbyname(socket.gethostname())
ip=0
port = 8580
tier2 = []
for x in range(5):
	tier2.append (webserveraddr + ":%d"%(8581+x))
	
print tier2


class Server(tierhandler):
	def do_GET(self):
		self.send_response(302)
		web_path = 'http://%s'%(tier2[ip])
		ip=ip+1
		if (ip >= len(tier2)):
			ip=0
		self.send_header('Location', web_path)
		self.end_headers()

SocketServer.TCPServer.allow_reuse_address = True
print "load balancer tier1 berjalan di ip %s port %d" % (webserveraddr,port)
SocketServer.TCPServer(("", port), Server).serve_forever()