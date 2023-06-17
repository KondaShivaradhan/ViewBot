# pip install -r requirements.txt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import subprocess
import getpass
import time
import threading

def execute_script():
    os.system('chrome.bat')

# Create a new thread
script_thread = threading.Thread(target=execute_script)

# Start the thread
script_thread.start()
print("Script execution completed.")
file_path = 'driver' 
# Specify the correct file path
print(file_path)

webdriver.Chrome(ChromeDriverManager(path=file_path).install())



# Open a URL in the Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
print('came here')
driver = webdriver.Chrome(executable_path='driver\\.wdm\\drivers\\chromedriver\\win32\\114.0.5735.90\\chromedriver.exe',options=chrome_options)
url = 'https://www.youtube.com/@aajtak/live'
driver.get(url)

# Rest of your code...

# Close the browser
driver.quit()
