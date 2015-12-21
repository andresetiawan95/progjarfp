import SocketServer;
import SimpleHTTPServer;
import sys;
serverhandler = SimpleHTTPServer.SimpleHTTPRequestHandler;
#round robin weighted
webserver = []
for i in range(10):
	webserver.append('IP:PORT')
for i in range (6)
	webserver.append('IP:PORT')
for i in range (4)
	webserver.append('IP:PORT')

class Server(serverhandler):
	def do_GET(self):
		self.send_response(302)
		web_path = 'http://10.151.34.105:9013'
		self.send_header('Location', web_path)
		self.end_headers()

port = 8822
SocketServer.TCPServer.allow_reuse_address = True
print "open socket in port %d" % (port)
SocketServer.TCPServer.request_queue_size = 10000
SocketServer.TCPServer(("", port), Server).serve_forever()

