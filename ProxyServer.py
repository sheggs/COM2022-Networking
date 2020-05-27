from socket import *
import sys
import webbrowser

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
print(sys.argv[1])
port = 5050;
print("Proxy started on port ",port)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', port))
tcpSerSock.listen(1);

#webbrowser.open('http://localhost:',port,'/google.com') 
# Fill in start.
# Fill in end.
while 1:
	# Strat receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	print("Connected.");
	message = tcpCliSock.recv(port);
	#print(message);
	filename = message.split()[1].partition("//")[2];
	print(filename)
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	c = socket(AF_INET, SOCK_STREAM);

	try:
		# Check wether the file exist in the cache
		f = open(filetouse[1:], "r")
		outputdata = f.readlines()
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")
		tcpCliSock.send("Content-Type:text/html\r\n")
		# Fill in start.
		# Fill in end.
		print('Read from cache')

	#Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			# Create a socket on the proxyserver
			proxyPort = 80
			# Fill in start.		# Fill in end.
			hostn = filename.replace("www.","",1)
			#requestGET = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % hostn
			print("Request Page (File not in cache): " + hostn)
			try:
				print("Trying")
				# Connect to the socket to port 80
				# Fill in start.
							
				c.connect((hostn,proxyPort))

				#c.connect(("google.com",80))

				#cClient, addr = c.accept()
				#c.send(requestGET.encode())
				#message = c.recv(proxyPort)
				#print(message)
				print("Trying to get data...")

				#print(message)
				# Fill in end.
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				fileobj = c.makefile('r', 0)
				print("2")

				fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
				print("3")

				# Read the response into buffer
				# Fill in start.
				buffer = fileobj.readlines()
				# Fill in end.
				# Create a new file in the cache for the requested file.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				print("buff reached")
				tmpFile = open("./" + filename,"wb")
				for l in buffer:
					tmpFile.write(l)
					tcpCliSock.send(l)
				# Fill in start.
				# Fill in end.

			except:
				print("Illegal request")
		else:
			print("hi");
			# HTTP response message for file not found
			# Fill in start.
			# Fill in end.
	# Close the client and the server sockets
	tcpCliSock.close() 
	c.close()

# Fill in start.		
# Fill in end.
