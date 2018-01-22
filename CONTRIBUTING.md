## For Contributors

#### Installing the repository
1. Make sure you have Sublime Text 3 installed. You can get it [here](https://www.sublimetext.com/3).
2. Open your command line and type in `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User`. This is where Sublime Text finds all of its plugins.
3. Clone the repository using `git clone`. 

#### Running the example plugin
1. In the repository, open up `example_plugin.py` in Sublime Text
2. Open the console in Sublime through `View > Show Console`
3. Open `plugin_test.txt` in another tab
4. While viewing `plugin_test.txt`, type in `view.run_command('example')` in the console. You should see `Hello, World!` show up in `plugin_test.txt`.