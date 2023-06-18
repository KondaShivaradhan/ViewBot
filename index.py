# pip install -r requirements.txt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
import os
import pytchat
import requests
import subprocess
import getpass
import time
import threading
import json
from jokeapi import Jokes  # Import the Jokes class
import threading
from random import randrange
def execute_script():
    os.system('chrome.bat')

# Create a new thread
script_thread = threading.Thread(target=execute_script)

# Start the thread
# path=file_path
script_thread.start()
print("Script execution completed.")
file_path = 'driver' 
driver_service = webdriver.chrome.service.Service(ChromeDriverManager(path=file_path).install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--remote-debugging-port=8989')
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
# driver = webdriver.Chrome(service=driver_service, options=chrome_options)
driver = webdriver.Chrome(executable_path='driver\\.wdm\\drivers\\chromedriver\\win32\\114.0.5735.90\\chromedriver.exe',options=chrome_options)
print('came here')

url = 'https://www.youtube.com/@blazingbane5565/live'
driver.get(url)
driver.implicitly_wait(10)
xpath_expression = '//meta[@property="og:url"]'
meta_element = driver.find_element_by_xpath(xpath_expression)
content = meta_element.get_attribute("content")
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='chatframe']"))
xpath="shiva"
xpath_expression = '//span[@id="author-name"]'
span_element = driver.find_element_by_xpath(xpath_expression)
text_content = span_element.text
print(text_content)
try:
    if driver.find_element_by_css_selector('#input-panel #container [aria-label="Chat publicly as '+BotName+'..."]').is_displayed():
        xpath='#input-panel #container [aria-label="Chat publicly as '+BotName+'..."]'
        print(BotName)
except Exception as e:
    print("Relangi not working xpath")
try:
    if driver.find_element_by_css_selector('#input-panel #container [aria-label="Say something..."]').is_displayed():
        xpath='#input-panel #container [aria-label="Say something..."]'
        print("yes say something")
except Exception as e:
    print("not say something xpath")
print(xpath)
def reply(data):
  print("funtion called with data - "+ data)
  driver.find_element_by_css_selector(xpath).clear()
  driver.find_element_by_css_selector(xpath).send_keys(data)
  driver.find_element_by_css_selector(xpath).send_keys(Keys.RETURN)
print(content)
index = content.index('v=')
vid = content[32:]
print('video id is here')
print(vid)
chat = pytchat.create(video_id=vid)
def printit():
  threading.Timer(randrange(60, 100), printit).start()
  url = 'https://raw.githubusercontent.com/KondaShivaradhan/cloud/main/responce.json'
  resp = requests.get(url)
  data = json.loads(resp.text)
#   print(data['random'])
  spam = data['random'][randrange(0, len(data['random']))]
  print(spam)
  reply(spam)
printit()
