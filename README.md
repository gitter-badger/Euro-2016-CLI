# Euro-2016-CLI

[![Join the chat at https://gitter.im/stvhwrd/Euro-2016-CLI](https://badges.gitter.im/stvhwrd/Euro-2016-CLI.svg)](https://gitter.im/stvhwrd/Euro-2016-CLI?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Requirements:

**You must replace `REDDIT_USERNAME` and `REDDIT_PASSWORD` in line #15 of streams.py with your own Reddit username and password.** 


### Features
Get live soccer/football streams, highlights and live stats for EURO 2016 directly from your terminal! (MAC)
  1. Find any live soccer/football streams within 3 seconds
  2. Find any EURO2016 highlights within 3 seconds
  3. Browse through live stats about the EURO 2016, fixtures, standings, etc...


### Install Pip and Python modules:

##### Pip

You may already have pip.  Enter the command `pip --version` to find out (if you get a version number, then you have it).
If you don't have pip, then install it:

`sudo easy_install pip`


### Python modules

`pip install praw termcolor lxml`


### Installing and Using the Utility:

On your command line, enter

1. `cd ~`  navigate to your home directory
2. `git clone https://github.com/stvhwrd/Euro-2016-CLI.git`  download the git repository to a new folder in your home directory
3. `cd Euro-2016-CLI`  navigate to the new folder containing the python files
4. `python ./main_menu.py` open the main file with python
5. Follow the on-screen prompts.  Input is not case-sensitive.

This utility was forked from [jctissier](https://github.com/jctissier/) with the intent of making it fully compatible with both Python2 and Python3 and conform to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).


### License:

[MIT](https://tldrlegal.com/license/mit-license) © Stevie Howard 2016
