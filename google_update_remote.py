import sublime
import sublime_plugin
import requests
import pickle

class GoogleUpdateRemoteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.active_window().run_command("login")
		client = requests.session()
		with open("cookie.txt","rb") as f:
			cookie = pickle.load(f)
			client.cookies = cookie
		path_to_file = self.view.file_name()
		f = open(path_to_file, "rb").read()
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		# a = client.post("http://localhost:8000/googledrive/update_remote", 
		a = client.post("http://sublimesync.herokuapp.com/googledrive/update_remote",
                  headers={"X-CSRFToken": client.cookies["csrftoken"]},
                   data={"text": f,"name": file_name})
		print(a.text)