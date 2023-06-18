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
script_thread.start()
print("Script execution completed.")
file_path = 'driver' 
# Specify the correct file path
print(file_path)

webdriver.Chrome(ChromeDriverManager(path=file_path).install())
# Open a URL in the Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
print('came here')
driver = webdriver.Chrome(executable_path='driver\\.wdm\\drivers\\chromedriver\\win32\\114.0.5735.90\\chromedriver.exe',options=chrome_options)
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

# Get the text content of the span element
text_content = span_element.text

# Print the text content
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
# xpath="#input-panel #container [aria-label='Chat publicly as '+BotName+'...']"
# xpath="#input-panel #container [aria-label='Say something... (slow mode is on)']"
# xpath="#input-panel #container [aria-label='Say something...']" 
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

while chat.is_alive():
     for c in chat.get().sync_items():
         try:
            chan = c.author.name
            msg = c.message.lower()
            print(msg)
            if(chan !=BotName):
             if(msg.startswith("fun ") or (" bor ") in msg or (" fun ") in msg or (" kills ") in msg):
                 try:
                    responce = [" Fun is subjective ", " when ever u kill a person remember that there is a human behind the charector ", " you have fun? ", " yes yes good play "]
                    data = chan +" "+ responce[randrange(0, len(responce))]
                    print("fun is triggered")
                    reply(data)
                 except:
                     print(" op deggara error ")
             if(msg.startswith("op ") or (" op ") in msg or (" nt") in msg or msg.startswith("nicetry") or ("nice try") in msg or (" nt ") in msg   ):
                 try:
                    responce = ["that was cool isnt it", " its natural he is a pro  ", " well that was intense,isnt it?", " yes yes good play "]
                    data = chan +" "+ responce[randrange(0, len(responce))]
                    reply(data)
                 except:
                     print(" op deggara error ")
         except Exception as e:
            print(e)