## For Contributors


### TODO:
* Heroku Server
* `DropboxRequest.py`: deal with invalid arguments
* Add OAuth2 functionality to plugin --> not sure how to go about this yet.
* Figure out environment variables for application key/secret.

#### Installing the repository
1. Make sure you have Sublime Text 3 installed. You can get it [here](https://www.sublimetext.com/3).
2. Open your command line and type in `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`. This is where Sublime Text finds all of its plugins.
3. Clone the repository using `git clone`. 

#### Running plugins
##### Run example plugin
1. In the repository, open up `example.py` in Sublime Text
2. Open the console in Sublime through `View > Show Console`
3. Type in `view.run_command('example')` in the console and look in the top left corner of the code document.


#### Jupyter Notebooks
Jupyter Notebooks can't be accessed from the ~/Library directory (at least I don't think so?), so if you want to use it, you'll need to move it to another location on your computer to work on it and copy it back into the git repository folder once you're finished.

##### External Libraries
Can only use default modules included in Python 3 and possibly a couple external ones, due to Sublime's Plugin API restrictions.
