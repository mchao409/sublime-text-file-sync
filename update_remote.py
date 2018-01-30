import sublime
import sublime_plugin
from .DropboxRequest import DropboxRequest
import os
import urllib
import urllib.request

class UpdateRemoteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		app_url = "/Users/michellec/Library/Application Support/Sublime Text 3/Packages/sublime-text-file-sync/app_info.txt"
		f = open(app_url, "r") ## Contains private info about application
		APP_KEY = f.readline().rstrip().replace("app key ", "")
		APP_SECRET = f.readline().rstrip().replace("secret ", "")
		token = f.readline().rstrip().replace("token", "")
		a = DropboxRequest(token)
		a.list_folder("")
		# print(self,0,a.list_folder(""))
