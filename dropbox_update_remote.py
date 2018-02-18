import sublime
import sublime_plugin
from .DropboxRequest import DropboxRequest
import os

class DropboxUpdateRemoteCommand(sublime_plugin.TextCommand):
	"""
	Overrides the content of the Dropbox-hosted file with the content of the current file.
	"""
	def run(self, edit):

		current_dir = os.getcwd()
		token = open(current_dir + "/sublime-text-file-sync-token.txt").readline()
		path_to_file = self.view.file_name()
		a = DropboxRequest(token)
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		dropbox_path = a.get_file_path(file_name)
		print(a.update_remote(dropbox_path,path_to_file))


