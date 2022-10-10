# Capitalize every nth letter of a string

## Problem statement
1 . Write a function that capitalizes *only* the nth alphanumeric character of a string, so that if I hand you

Aspiration.com

and I ask you to capitalize every 3rd character, you hand me back

asPirAtiOn.cOm

If I ask you to capitalize every 4th character, you hand me back

aspIratIon.cOm

Please note: 
* Characters other than each nth should be downcased
* For the purposes of counting and capitalizing every three characters, consider only alphanumeric
  characters, ie `[a-z][A-Z][0-9]`.

## Language choice
I chose to use Python to solve this problem because Python makes string manipulation so easy. 
Solving problems is easiest when we have and use the right tool.

This application requires Python 3.7 or higher.

## Files for submission

For simplicity, all files are in the project's root folder. If this were a larger problem, I would add folders
to group classes, scripts, and tests accordingly.

* main.py - Contains the definition of the main function and `capitalize_nth_letter`
* test_capitalization.py - Contains test methods to test `capitalize_nth_letter` under various input scenarios, 
including scenarios that should raise an exception.

## Dependencies
The following dependencies need to be installed.
* `re` - Regex library
* `pytest` - testing framework 

Python packages can be installed in the virtual environment within PyCharm with the following steps:
* Go to `View` -> `Tool Windows` -> `Python Packages`
* Search for the package
* Click `install`

Install Python packages via the command line:

`> pip3 install <package_name>`

## Running/Testing
* Via PyCharm
  * Both the test file and main can be run through PyCharm's play buttons that appear in the gutter of the file.
* Via commandline
  * Run `main.py` by executing the following steps:
    * Navigate to the folder containing the test
    * Run `> python main.py`
  * Run `test_capitalization.py` by executing the following steps:
    * Navigate to the folder containing the test
    * Run `> pytest` 
