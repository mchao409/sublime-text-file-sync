import urllib
import json

# TODO: Dealing with invalid arguments


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
            req = urllib.request.Request(url,json.dumps(data).encode(),headers)


        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")
    
    def get_file_id(self,file_name):
        """Gets the Dropbox id of a file
        Args:
            file_name: Requested id's file name
        Returns: 
            String of file_name's id
        """
        list_files = self.list_folder("")
        for file_info in list_files:
            if file_info["name"].lower() == file_name.lower():
                return file_info["id"]
        return "NOT FOUND" ## Throw Exception -- need to implement
    
    def list_folder(self,path):
        """ Gets a list of all files in a folder
        Args: 
            path: string path to the folder to look in
        Returns: a dict containing information about that folder
        """
        url = "https://api.dropboxapi.com/2/files/list_folder"
        headers = {"Authorization": "Bearer " + self.token,
                  "Content-Type": "application/json"}
        data = {"path": path,
               "recursive": True}
        return json.loads(DropboxRequest.make_request(url, headers,data=data))["entries"]
    
    def download(self,name):
        """Grabs the content of the file currently hosted on Dropbox
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
