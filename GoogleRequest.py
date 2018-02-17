import urllib
import json

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class GoogleRequest:
    def __init__(self,token):
        self.token = token

    @staticmethod
    def make_request(url, headers, data=None):
        """ Makes a request to Google's API
        Args:
            url of call, headers of call, optional data
        Returns:
            Request string
	Need to figure out how to do PATCH method with urllib
        """
        if(data == None):
            req = urllib.request.Request(url,None,headers)
        else:
            req = urllib.request.Request(url,data,headers)
#             req = urllib.request.Request(url,json.dumps(data).encode(),headers)
        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")

    def get_file_id(self,file_name):
        """ Gets the Google id of a file
        Args:
            file_name: Requested id's file name
        Returns:
            String of file_name's id
        """
        list_files = self.list_folder()
        for file_info in list_files:
            if file_info["name"].lower() == file_name.lower():
                return file_info["id"]
        raise InputError(file_name, "File Not Found")

    def get_file_path(self,file_name):
        """ Gets the Google path of a file
        Args:
            file_name: Name of file to get path
        Returns:
            String, path to file_name
        """
        list_files = self.list_folder()
        for file_info in list_files:
            if file_info["name"].lower() == file_name.lower():
                return file_info["path_lower"]
        raise InputError(file_name, "File Not Found")

    def list_folder(self):
        """ Gets a list of all files locally hosted in Google
        Args:
            path: string path to the folder to look in
        Returns: a dict containing information about that folder
        """
        url = "https://www.googleapis.com/drive/v3/files"
        headers = {"Authorization": "Bearer " + self.token,
                  "Content-Type": "application/json"}
        data = {"corpora": "user"}
        return json.loads(GoogleRequest.make_request(url, headers,data=json.dumps(data).encode()))["files"]

    def download(self,name):
        """ Grabs the content of the file currently hosted on Google
        Args:
            name: The name of the file
        Returns:
            A string containing the content of the corresponding file in Google
	Why do we get redirect status here?
        """
        file_id = self.get_file_id(name)
        url = "https://www.googleapis.com/drive/v3/files/" + file_id + “?alt=media”
        headers = {
            "Authorization": "Bearer " + self.token,
        }
        return GoogleRequest.make_request(url, headers)

    def update_remote(self, file_id, path_to_file):
        """ Updates the content of the file currently hosted on Google with the given file.
           If content is not there, the file will be created on Google
        Args:
            file_id: the ID of the file on Google
            path_to_file: the local path to the file
        Returns:
            a json file
	This command was successful in updating remote content:
		curl -X PATCH  -d "@data.txt" -H "Content-Type: multipart/mixed" "https://www.googleapis.com/upload/drive/v3/files/11G-DKcActbNNA4PPCuF_oNLSeHjeitm4unxoXTerrxA?uploadType=media&access_token=ya29.GltlBZeVqPMUbQ61QkFb2Dzxs_kmvsl63AogGI36TDn1YBYfTpZNGKEzRr68FM-UCQQntAb29NVPtg8xCa8n45y1zR9Hz_YVrNMX_CaBCpocdQGYvtHmNmL57hkA"
        """
        url = "https://www.googleapis.com/upload/drive/v3/files/" + file_id + “?uploadType=media"
        headers = {
                "Authorization": "Bearer " + self.token,
                "Content-Type": "application/octet-stream"
        }
        data = None
    	try:
		    data = open(path_to_file, "rb").read()
        except IOError:
            print "Could not read file:", path_to_file
			raise
        return GoogleRequest.make_request(url,headers,data)
