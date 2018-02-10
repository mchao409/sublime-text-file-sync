import sublime
import sublime_plugin
import webbrowser
import socket
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import socketserver
import time
import re
from . import token_server


class AuthenticateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("hello")
		webbrowser.open("http://localhost:8000")

		# run_server()


