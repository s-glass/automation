# Lab - Class 19
## Project: automation

Author: Sarah Glass for Python 401
Worked with Anthony, Slava, and Jared at a Remo table.

## Overview

Your team is working on a project to improve the organization and automation of various tasks. This includes handling user data, sorting files, parsing logs, and other miscellaneous tasks. You’ll be writing Python scripts to automate these tasks and make your team’s work more efficient.

Feature Tasks and Requirements:

(1) Automate the creation of a folder.
Write a Python script to create a new folder with a specified name.

(2) Handle a deleted user.
user2 is a deleted user and need to move their documents from their user folder to a temporary folder. Your script will create the temporary folder. This will effectively delete the user from the system while still maintaining a record of their documents.

(3) Sort documents into appropriate folders.
Go through a given folder and sort the documents into additional folders based on their file type.
Move log files into a logs folder. If a logs folder doesn’t exist, your script should create one.
Move email files into a mail folder. If a mail folder doesn’t exist, your script should create one.

(4) Parse a log file for errors and warnings.
From the previous task, you’ve moved a log file into the logs folder. Now, parse the log file for errors and warnings and create two separate log files in a target directory:
errors.log: Contains all error messages.
warnings.log: Contains all warning messages.

(5) Create a menu-driven application.
Give the user a list of automation tasks (1-4) and let them choose one to execute. Customize your application by incorporating an additional automation task, choose one:
Counting the number of specific file types in a directory.
Renaming files based on a specific pattern.
Automatically backing up specific folders.

## Links and Resources

* TA and peer help.
* Reviewing recorded lecture.
* ChatGPT prompting.


## Setup

No .env requirements; gitignore invludes venv.

## How to initialize/run your application

* python3 -m automation.create_folder
* python3 -m automation.delete_user
* python3 -m automation.menu_tasks
* python3 -m automation.parse_files
* python3 -m automation.sort_docs

## Libraries

* os, shutil, sys, rich

## Tests

Still need to add testing.

* pytest tests/test_automation.py