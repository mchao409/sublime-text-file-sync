import sublime, sublime_plugin
import requests
import pickle
import webbrowser
import ssl
class LoginCommand(sublime_plugin.WindowCommand):

    def run(self):
        if not self.check_if_logged_in():
            print("not logged in")
            self.temp_pass = ""
            self.window.show_input_panel("Your username:", '', lambda s: self.username_callback(s), 
                None, None)
        # else:
            # sublime.message_dialog("You're already logged in")

    def username_callback(self, text):
        username = text
        self.window.show_input_panel("Your password:", '', 
            lambda s: self.login(username,s), None,None)

    def login(self, username,password):
        client = requests.session()
        r = client.get("http://sublimesync.herokuapp.com/login")
        # print(r.cookies['csrftoken'])
        # r = client.get("http://localhost:8000/login")
        l = client.post("http://sublimesync.herokuapp.com/login", 
        # l = client.post("http://localhost:8000/login", 
                 data={"username": username, "password": password},
                  headers={"X-CSRFToken":r.cookies["csrftoken"]},
                 cookies=r.cookies)
        print(l.text)
        if len(l.cookies) == 0 or ("error" in l.text.lower()):
            sublime.message_dialog("Failed to login.")
        else:
            sublime.message_dialog("You've been logged in.")
            # print("here is the page")
            with open("cookie.txt", "wb") as f:
                # print(client.cookies)
                pickle.dump(client.cookies, f)
            # with open("cookie.txt", "rb") as f:
            #     print(pickle.load(f))

    def check_if_logged_in(self):
        client = requests.session()
        try:
            with open("cookie.txt","rb") as f:
                cookie = pickle.load(f)
                client.cookies = cookie
                page = client.post("http://sublimesync.herokuapp.com",
                # page = client.post("http://localhost:8000/", 
                    headers={"X-CSRFToken":client.cookies["csrftoken"]})
                # print(page.text)
                if "logout" in page.text.lower():
                    # sublime.message_dialog("You're already logged in")
                    return True
        except:
            print("error occurred")
            return False
        r = client.get("http://sublimesync.herokuapp.com")
        # r = client.get("http://localhost:8000")
        if len(r.cookies) == 0:
            pass
            return False
        return True







