import sublime, sublime_plugin
import requests
import pickle
class LoginCommand(sublime_plugin.WindowCommand):

    def run(self):
        # open an input box for some user input
        if not self.check_if_logged_in():
            self.temp_pass = ""
            self.window.show_input_panel("Your username:", '', lambda s: self.username_callback(s), 
                lambda s: self.hide_pass(self,s,username), None)

    def username_callback(self, text):
        username = text
        self.window.show_input_panel("Your password:", '', 
            lambda s: self.login(username,s), None,None)

    def login(self, username,password):
        client = requests.session()
        r = client.get("http://localhost:8000/login")
        l = requests.post("http://localhost:8000/login/", 
                 data={"username": "mchao409", "password": "Qazxcvbnm123"},
                  headers={"X-CSRFToken":r.cookies["csrftoken"]},
                 cookies=r.cookies)

        if(len(l.cookies) == 0):
            sublime.message_dialog("Failed to login. Please try again.")
        else:
            sublime.message_dialog("You've been logged in.")
            with open("cookie.txt", "wb") as f:
                pickle.dump(r.cookies, f)

            with open("cookie.txt", "rb") as f:
                print(cookie.load(f))


    def check_if_logged_in(self):
        try:
            with open("cookie.txt","r") as f:
                print(pickle.load(f))
        except:
            return False


        client = requests.session()
        r = client.get("http://localhost:8000")
        if len(r.cookies) == 0:
            pass
            return False
        return True






