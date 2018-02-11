import sublime
import sublime_plugin
import socket
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import socketserver
import webbrowser
import re
import os
# from . import token_server
from subprocess import Popen
import threading
from Crypto.Cipher import AES

class AuthenticateCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		server = ServerThread(name="token_server")
		server.start()


class ServerThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self, name=name)

	def run(self):
		run_server()


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for the server.
    """
    def handle(self):
        print("HANDLING REQUEST")
        # self.request is the TCP socket connected to the client
        text = self.request.recv(1024).strip()
        if "token" in text.decode("utf-8"):
            data = text.decode("utf-8")
            # print(data)
            self.request.sendall("HTTP/1.1 200 OK\n".encode())
            token = re.search("(?<=token=)(.*?)(?=[!\s])", data).group()
            current_dir = os.getcwd()
            with open(current_dir + "/sublime-text-file-sync-token.txt", "w") as f:
            	f.write(token)

def run_server():
    HOST, PORT = "localhost", 8001

    # Create the server, binding to localhost on port 8001
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print("Server created")
    webbrowser.open("http://localhost:8000/redirect")
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    try:
#         server.serve_forever()
        print("Serving server")
        server.handle_request()
        server.server_close()
    except:
        server.server_close()

