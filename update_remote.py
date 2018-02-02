import sublime
import sublime_plugin
from .DropboxRequest import DropboxRequest


class UpdateRemoteCommand(sublime_plugin.TextCommand):
	"""
	Overrides the content of the Dropbox-hosted file with the content of the current file.
	"""
	def run(self, edit):
		# Get app key, secret, token -- private file
		app_url = "/Users/michellec/Library/Application Support/Sublime Text 3/Packages/sublime-text-file-sync/app_info.txt"
		f = open(app_url, "r") # Contains private info about application
		APP_KEY = f.readline().rstrip().replace("app key ", "")
		APP_SECRET = f.readline().rstrip().replace("secret ", "")
		token = f.readline().rstrip().replace("token ", "")
		path_to_file = self.view.file_name()
		a = DropboxRequest(token)
		file_name = path_to_file[path_to_file.rfind("/")+1:]
		dropbox_path = a.get_file_path(file_name)
		print(a.update_remote(dropbox_path,path_to_file))


