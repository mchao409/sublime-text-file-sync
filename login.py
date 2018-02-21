import sublime, sublime_plugin
import requests
class LoginCommand(sublime_plugin.WindowCommand):
    def run(self):
        # open an input box for some user input

        self.window.show_input_panel("Your username:", '', lambda s: self.username_callback(s), None, None)

    def username_callback(self, text):
    # now try to write this text to the panel
    	username = text
    	self.window.show_input_panel("Your password:", '', 
    		lambda s: self.password_callback(username,s), None,None)




    def check_if_logged_in(self):
    	pass
    # def get_us(self,username,password):




