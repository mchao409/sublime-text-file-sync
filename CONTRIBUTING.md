## For Contributors

* [Django server](https://github.com/mchao409/sublimeserver)

#### Installing the repository
1. Make sure you have Sublime Text 3 installed. You can get it [here](https://www.sublimetext.com/3).
2. Open your command line and type in `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`. This is where Sublime Text finds all of its plugins, for MacOS.
3. Fork the repository and clone the fork into this folder using `git clone <fork url>`. 
4. Making a pull request: Please explain clearly in the body of your PR the changes you made to the repository.

#### Running plugins

You can read up the documentation on Sublime Text 3 plugins [here](https://www.sublimetext.com/docs/3/api_reference.html).

##### External Libraries
This repository can only default modules included in Python 3, unless the source code for a separate module is added in the `lib` folder, due to Sublime's Plugin API restrictions. Currently, only the `requests` module is there.
