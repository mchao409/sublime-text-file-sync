import sublime
import sublime_plugin
import os
import requests
import pickle

class DropboxUpdateRemoteCommand(sublime_plugin.TextCommand):
	"""
	Overrides the content of the Dropbox-hosted file with the content of the current file.
	"""
	def run(self, edit):
		sublime.active_window().run_command("login")
		client = requests.session()
		with open("cookie.txt","rb") as f:
			cookie = pickle.load(f)
			client.cookies = cookie
		path_to_file = self.view.file_name()
		f = open(path_to_file, "rb").read()
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		# print(client.post("http://localhost:8000/dropbox/update_remote", 
		print(client.post("http://sublimesync.herokuapp.com/dropbox/update_remote",
                  headers={"X-CSRFToken": client.cookies["csrftoken"]},
                   data={"text": f,"name": file_name}).text)
		


