import sublime
import sublime_plugin
import requests
import pickle

class GoogleUpdateLocalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.active_window().run_command("login")
		client = requests.session()
		with open("cookie.txt","rb") as f:
			cookie = pickle.load(f)
			client.cookies = cookie
		# print(client.cookies)
		path_to_file = self.view.file_name()
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		a = client.post("http://sublimesync.herokuapp.com/googledrive/update_local",
		# a = client.post("http://localhost:8000/googledrive/update_local",
                  headers={"X-CSRFToken": client.cookies["csrftoken"]},
                   data={"name": file_name})
		print(a.text)
		# print(a.text)
		# self.view.erase(edit, sublime.Region(0,self.view.size()))
		# self.view.insert(edit, 0, a.text)




