import sublime
import sublime_plugin
import socket
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import socketserver
import time
import re
import os
# from . import token_server
from subprocess import Popen

class AuthenticateCommand(sublime_plugin.WindowCommand):
	def run(self, edit, should_authenticate=False):
		# os.system("python server/token_server.py")
		d = os.getcwd()
		d += "/server/token_server.py"
		# Popen(["python", "-u", "server/token_server.py"],shell=True)
		HOST, PORT = "localhost", 8001
		# run_server()


		# webbrowser.open("http://localhost:8000/redirect")

		# token_server.run_server()



class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for the server.
    """
    def handle(self):
        print("HANDLING REQUEST")
        # self.request is the TCP socket connected to the client
        text = self.request.recv(1024).strip()
        print(text)
        if "token" in text.decode("utf-8"):
            data = text.decode("utf-8")
            print(data)
            self.request.sendall("HTTP/1.1 200 OK\n".encode())
            token = re.search("(?<=token=)(.*?)(?=[!\s])", data).group()
            with open("token.txt", "w") as f:
                f.write(token)
            f.close()

def run_server():
    HOST, PORT = "localhost", 8001

    # Create the server, binding to localhost on port 8001
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
