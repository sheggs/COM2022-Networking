from socket import *
import sys
port = 3000


print("Running on port ", port)
if len(sys.argv) <= 1:
    print(
        'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('', port))
tcpSerSock.listen(1)
# Fill in end.
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)
    # Fill in end.
    print("Browser Request:", message)
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    # print("Boo")
    # print("Testing",filename)
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        print("File found in cache ", filetouse)
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        for l in outputdata:
            tcpCliSock.send(l)
            print("Reading data from cache....")
            # Fill in end.

        print("Hi File Exists: " + fileExist)
        # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            print("FILE FALSE")
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            # Fill in start.		# Fill in end.
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                is404 = False
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('r', 0)
                fileobj.write("GET "+"http://" +
                              filename + " HTTP/1.0\r\n\r\n")
                # Read the response into buffer
                # Fill in start.
                buffer = fileobj.readlines()
                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                cleanedArray = []
                # Fill in start.
                for l in buffer:
                    if (l == "HTTP/1.0 404 Not Found\r\n"):
                        is404 = True
                    # There are problems with HREF = "/" SRC = "/" etc
                    l = l.replace('src=\"//', 'src = \" http://' + filename + '/')
                    l = l.replace(
                        'href = \"//', 'href = http://' + filename + '/')
                    l = l.replace(
                        'src=\"/', 'src = \" http://' + filename + '/')
                    l = l.replace(
                        'href=\"/', 'href = http://' + filename + '/')
                    l = l.replace(
                        'src=\"./', 'src = \" http://' + filename + '/')
                    l = l.replace(
                        'href=\"./', 'href = http://' + filename + '/')
                    cleanedArray.append(l)
                    # Fill in end.
                # if is404:
                #     print("404 Error Recieved")
                #     tmpFile.write("HTTP/1.0 404 Not Found\r\n")
                #     tmpFile.write("Content-type:text/html \r\n")
                #     tmpFile.write("<!DOCTYPE html>\r\n")
                #     tmpFile.write("<html>\r\n")
                #     tmpFile.write("<h1>\r\n")
                #     tmpFile.write("404 Error Returned\r\n")
                #     tmpFile.write("</h1>\r\n")
                #     tmpFile.write("</html> \r\n")

                else:
                    for line in cleanedArray:
                        tmpFile.write(line)
                        tcpCliSock.send(line)
                        print("EachLine: ", line)
                tmpFile.close()
            except gaierror:
                tcpCliSock.send("HTTP/1.0 404 Not Found\r\n")
                tcpCliSock.send("Content-type:text/html \r\n")
            except Exception as inst:
                print("Illegal request ", hostn, inst)
        else:
            hostn = filename.replace("www.", "", 1)
            print("404 Error: ", hostn)
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n")
            tcpCliSock.send("Content-type:text/html \r\n")
            # tcpCliSock.send("<!DOCTYPE html>")
            # tcpCliSock.send("<html>")
            # tcpCliSock.send("404 Not Found")
            # tcpCliSock.send("</html>")

            # HTTP response message for file not found
            # Fill in start.
            # Fill in end.
        # Close the client and the server sockets
        tcpCliSock.close()
        # c.close()

# Fill in start.
# Fill in end.
