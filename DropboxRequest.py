class DropboxRequest:
    def __init__(self,token):
        self.token = token
        
    @staticmethod
    def make_request(url, headers, data=None):
        """ Makes a request to Dropbox's API
        Args: 
            url, headers of call
        Returns: 
            a dict object
        """
        if(data == None):
            req = urllib.request.Request(url,None,headers)
        else:
            req = urllib.request.Request(url,json.dumps(data).encode(),headers)


        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")

    def list_folder(self,path):
        """ Gets a list of all files in a folder
        Args: 
            path: string path to the folder to look in
        Returns: a dict containing information about that folder
        """
        url = "https://api.dropboxapi.com/2/files/list_folder"
        headers = {"Authorization": "Bearer " + self.token,
                  "Content-Type": "application/json"}
        data = {"path": path}
        return DropboxRequest.make_request(url, headers,data=data)
    
    def download(self,path):
        url = "https://content.dropboxapi.com/2/files/download"

        headers = {
    "Authorization": "Bearer " + self.token,
    "Dropbox-API-Arg": '{"path":"/my-plugin.py"}'
        }
        
        return DropboxRequest.make_request(url, headers)

        
        