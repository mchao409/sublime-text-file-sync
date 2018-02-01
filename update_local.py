import sublime
import sublime_plugin
from .DropboxRequest import DropboxRequest
import os
import re

class UpdateLocalCommand(sublime_plugin.TextCommand):
	"""
	Updates the local window with the file that is hosted on Dropbox. 
	"""
	def run(self, edit):
		# Get app key, secret, token -- private file
		app_url = "/Users/michellec/Library/Application Support/Sublime Text 3/Packages/sublime-text-file-sync/app_info.txt"
		f = open(app_url, "r") ## Contains private info about application
		APP_KEY = f.readline().rstrip().replace("app key ", "")
		APP_SECRET = f.readline().rstrip().replace("secret ", "")

		# Will eventually need to use server for oauth
		token = f.readline().rstrip().replace("token ", "")

		a = DropboxRequest(token)
		path_to_file = self.view.file_name()
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		print(file_name)
		text = a.download(file_name)

		# Replace the current text in the file....
		self.view.erase(edit, sublime.Region(0,self.view.size()))

		# ... with the text in the locally-hosted file
		self.view.insert(edit, 0, text)
		