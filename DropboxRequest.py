import urllib
import json

# TODO: Dealing with invalid arguments
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

	
class DropboxRequest:
    def __init__(self,token):
        self.token = token
        
    @staticmethod
    def make_request(url, headers, data=None):
        """ Makes a request to Dropbox's API
        Args: 
            url of call, headers of call, optional data
        Returns: 
            Request string
        """
        if(data == None):
            req = urllib.request.Request(url,None,headers)
        else:
            req = urllib.request.Request(url,data,headers)
#             req = urllib.request.Request(url,json.dumps(data).encode(),headers)
        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")
    
    def get_file_id(self,file_name):
        """ Gets the Dropbox id of a file
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
        """ Gets the Dropbox path of a file
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
    
    def list_folder(self,file_path=""):
        """ Gets a list of all files locally hosted in Dropbox
        Args: 
            file_path: string path to the folder to look in
        Returns: a dict containing information about that folder
        """
        url = "https://api.dropboxapi.com/2/files/list_folder"
        headers = {"Authorization": "Bearer " + self.token,
                  "Content-Type": "application/json"}
        data = {"path": file_path,
               "recursive": True}
        return json.loads(DropboxRequest.make_request(url, headers,data=json.dumps(data).encode()))["entries"]
    
    def download(self,name):
        """ Grabs the content of the file currently hosted on Dropbox
        Args: 
            name: The name of the file
        Returns:
            A string containing the content of the corresponding file in Dropbox
        """
        file_id = self.get_file_id(name)
        url = "https://content.dropboxapi.com/2/files/download"
        headers = {
            "Authorization": "Bearer " + self.token,
            "Dropbox-API-Arg": "{\"path\":\"" + file_id + "\"}"
        }
        return DropboxRequest.make_request(url, headers)
    
    def update_remote(self, dropbox_path, path_to_file):
        """ Updates the content of the file currently hosted on Dropbox with the given file.
           If content is not there, the file will be created on Dropbox
        Args: 
            dropbox_path: the path to the file on Dropbox
            path_to_file: the local path to the file
        Returns:
            a json file 
        """
        url = "https://content.dropboxapi.com/2/files/upload"
        headers = {
                "Authorization": "Bearer " + self.token,
                "Content-Type": "application/octet-stream",
                "Dropbox-API-Arg": "{\"path\":\"" + dropbox_path + "\",\"mode\":{\".tag\":\"overwrite\"}}"
        }
        data = None
   #      try:
   #          data = open(path_to_file, "rb").read()
   #      except IOError:
   #          print ("Could not read file:", path_to_file)
			# raise
        return DropboxRequest.make_request(url,headers,data)
            