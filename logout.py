import sublime
import sublime_plugin
import requests
import pickle

class LogoutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.logout()

    def logout(self):
        if self.check_if_logged_in():
            client = requests.session()
            try:
                with open("cookie.txt", "rb") as f:
                    cookie = pickle.load(f)
                    client.cookies = cookie
                    page = client.get("http://sublimesync.herokuapp.com",
                    # page = client.get("http://localhost:8000/logout", 
                        headers={"X-CSRFToken": client.cookies["csrftoken"]})
                open("cookie.txt").close()
            except:
                print("Error occured in logout")
                pass
            sublime.message_dialog("You've been logged out.")

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

