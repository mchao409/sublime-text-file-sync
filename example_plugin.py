import sublime
import sublime_plugin



class DuplicateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		import oauthlib
		import os
		import sys
		sys.path.insert(0,os.path.dirname("google-api-client-master"))
		self.view.insert(edit, 0, "Hello, World!")




