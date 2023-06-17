from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import subprocess
import getpass
import time

# Get the currently logged-in user account name
username = getpass.getuser()
command = 'chrome.exe --remote-debugging-port=8989'
working_directory = 'C:\\Program Files\\Google\\Chrome\\Application'
subprocess.run(command, shell=True, cwd=working_directory)