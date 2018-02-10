import webbrowser
import socket
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import socketserver
import time
import re
class MyTCPHandler(socketserver.BaseRequestHandler):
    data = None
    """
    The request handler class for the server.
    """
    def handle(self):
        print("HANDLING REQUEST")
        # self.request is the TCP socket connected to the client
        text = self.request.recv(1024).strip()
#         print(text)
        if MyTCPHandler.data == None and "token" in text.decode("utf-8"):
            MyTCPHandler.data = text.decode("utf-8")
            print(MyTCPHandler.data)
            self.request.sendall("HTTP/1.1 200 OK\n".encode())
            token = re.search("(?<=token=)(.*?)(?=[!\s])", MyTCPHandler.data).group()
            with open("token.txt", "w") as f:
                f.write(token)
#             print("here is the data: ")
#             print(MyTCPHandler.data)

def run_server():
    HOST, PORT = "localhost", 8001

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print("Server created")

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    try:
#         server.serve_forever()
        print("Serving server")
        server.handle_request()
        server.server_close()
    except:
        server.server_close()


run_server()