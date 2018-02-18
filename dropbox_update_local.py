import sublime
import sublime_plugin
from .DropboxRequest import DropboxRequest
import os

class DropboxUpdateLocalCommand(sublime_plugin.TextCommand):
	"""
	Updates the local window with the file that is hosted on Dropbox. 
	"""
	def run(self, edit):
		current_dir = os.getcwd()
		token = open(current_dir + "/sublime-text-file-sync-token.txt").readline()
		print(token)

		a = DropboxRequest(token)
		path_to_file = self.view.file_name()
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		text = a.download(file_name)

		# Replace the current text in the file....
		self.view.erase(edit, sublime.Region(0,self.view.size()))

		# ... with the text in the locally-hosted file
		self.view.insert(edit, 0, text)
		