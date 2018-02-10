import sublime
import sublime_plugin



class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		import http.server
		from urllib import request
		import urllib
		import json
		asdasd
		self.view.insert(edit,0,"Hello World!")
		# r = urllib.request.urlopen(url)
		# webbrowser.open(url,new=0,autoraise=True)

	

