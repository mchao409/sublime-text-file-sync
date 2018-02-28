# Sublime Text File Synchronization

This is a plugin for Sublime Text that allows you to to synchronize your files using hosting services such as Google Drive, Dropbox, and OneDrive, allowing you to access the same file on different machines. (Currently in development!)

For the server component of this project, please click [here](https://github.com/mchao409/sublimeserver)

##### How to use this
Note: Only currently tested for MacOSX
1. Download Sublime Text 3
2. Navigate to `~/Library/Application Support/Sublime Text 3/Packages` and clone the repository
3. Go to [this](https://sublimesync.herokuapp.com) website, create an account, and authorize the application with Dropbox and/or Google Drive.
4. Go back to Sublime Text 3, login by right-clicking and going to `Sublime-Sync > Login`
5. To upload/update a remote server's file, click `Update Remote`. To update a remotely saved file to your current view, click `Update Local`. The names of the files you would like to save should be identical, and there should not be files with the same names in your remote server (at this time).
6. To logout, navigate to `Sublime-Sync>Logout`

##### Functions: 
* Upload files to and grab updated files from hosting services.

#### Want to contribute?
Head over to the [CONTRIBUTING guide](CONTRIBUTING.md)




