import sublime
import sublime_plugin
import webbrowser

class SignupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		webbrowser.open("http://localhost:8000/signup")
