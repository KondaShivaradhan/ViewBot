# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import os
# import subprocess
# import getpass

# # Get the currently logged-in user account name
# username = getpass.getuser()
# command = 'chrome.exe --remote-debugging-port=8989'
# working_directory = 'C:\\Program Files\\Google\\Chrome\\Application'
# subprocess.run(command, shell=True, cwd=working_directory)
# file_path = 'driver'
# print(file_path)
# # Check if the path is a file
# if os.path.isfile(file_path):
#     print(f"The path '{file_path}' points to a file.")
# else:
#     print(f"The path '{file_path}' does not point to a file or the file does not exist.")
#     driver = webdriver.Chrome(ChromeDriverManager(path=file_path).install())
# # Open a URL in the Chrome browser
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
# driver = webdriver.Chrome(options=chrome_options)
# url = 'https://www.youtube.com/@aajtak/live'
# driver.get(url)

# # C:\Program Files\Google\Chrome\Application
# # driver.quit()
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
