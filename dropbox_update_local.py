import sublime
import sublime_plugin
import os
import requests
import pickle

class DropboxUpdateLocalCommand(sublime_plugin.TextCommand):
	"""
	Updates the local window with the file that is hosted on Dropbox. 
	"""
	def run(self, edit):
		self.view.run_command("login")
		client = requests.session()
		with open("cookie.txt","rb") as f:
			cookie = pickle.load(f)
			client.cookies = cookie
		path_to_file = self.view.file_name()
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		# a = client.post("http://localhost:8000/dropbox/update_local", 
		a = client.post("https://sublimesync.herokuapp.com/dropbox/update_local",
                  headers={"X-CSRFToken": client.cookies["csrftoken"]},
                   data={"name": file_name})		
		# text = a.download(file_name)
		# # Replace the current text in the file....
		self.view.erase(edit, sublime.Region(0,self.view.size()))
		# # ... with the text in the locally-hosted file
		self.view.insert(edit, 0, a.text)

	def update_local(self):
		pass
		