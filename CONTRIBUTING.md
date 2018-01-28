## For Contributors

#### Installing the repository
1. Make sure you have Sublime Text 3 installed. You can get it [here](https://www.sublimetext.com/3).
2. Open your command line and type in `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`. This is where Sublime Text finds all of its plugins.
3. Clone the repository using `git clone`. 

#### Running the example plugin
1. In the repository, open up `example_plugin.py` in Sublime Text
2. Open the console in Sublime through `View > Show Console`
3. Open `plugin_test.txt` in another tab
4. While viewing `plugin_test.txt`, type in `view.run_command('example')` in the console.

#### Jupyter Notebooks
Jupyter Notebooks can't be accessed from the ~/Library directory (at least I don't think so?), so you'll need to move it to another location on your computer to work on it and copy it back into the git repository folder once you're finished.

##### External Libraries
Can only use default modules included in Python 3 -- there are dependencies available for external libraries, but many do not seem to work, so sticking with default installed libraries is the safest bet.