import tkinter as tk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import shutil
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
window = tk.Tk()
window.title("Viewer Bot")

label = tk.Label(window, text="Viewer Bot by BlazingBane")
label.pack()

button = tk.Button(window, text="Start Bot")
button.pack()
def deleteDriver():
    directory = 'driver'  # Replace with the directory path you want to delete
    if os.path.exists(directory):
        
        shutil.rmtree(directory)
        print(f"The directory '{directory}' has been deleted.")
    else:
        print(f"The directory '{directory}' does not exist.")
    
def button_click():
    label.configure(text="Button Clicked!")
    deleteDriver()
    def execute_script():
        os.system('chrome.bat')
    script_thread = threading.Thread(target=execute_script)

    # path=file_path
    script_thread.start()
    print("Script execution completed.")
    file_path = 'driver' 
    driver_service = webdriver.chrome.service.Service(ChromeDriverManager(path=file_path).install())
    print("installed execution completed.")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--remote-debugging-port=8989')
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    print('came here')

    url = 'https://www.youtube.com/channel/UCPFM_Ug62Ei3CUfvquG4KOg/live'
    driver.get(url)
    driver.implicitly_wait(10)
    xpath_expression = '//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]'
    meta_element = driver.find_element_by_xpath(xpath_expression)
    print(meta_element.get_attribute('video-id'))
    content = meta_element.get_attribute('video-id')
    print('checking if the bottom is liked')
    element = driver.find_element_by_xpath("//body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[2]/ytd-watch-metadata[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ytd-menu-renderer[1]/div[1]/ytd-segmented-like-dislike-button-renderer[1]/yt-smartimation[1]/div[1]/div[1]/ytd-toggle-button-renderer[1]/yt-button-shape[1]/button[1]")
    aria_pressed = element.get_attribute("aria-pressed")
    print(aria_pressed)
    if(aria_pressed=='false'):
        element.click()
    else:
        print('already liked')
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='chatframe']"))
    xpath="shiva"
    xpath_expression = '//body/yt-live-chat-app[1]/div[1]/yt-live-chat-renderer[1]/iron-pages[1]/div[1]/div[1]/iron-pages[1]/div[1]/yt-live-chat-message-input-renderer[1]/div[1]/div[1]/div[1]/yt-live-chat-author-chip[1]/span[2]'
    span_element = driver.find_element_by_xpath(xpath_expression)
    BotName = span_element.text
    print('bot name is')
    print(BotName)
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
    vid = content
    print('video id is here')
    print(vid)
    chat = pytchat.create(video_id=vid)
    def printit():
        threading.Timer(randrange(60, 100), printit).start()
        url = 'https://raw.githubusercontent.com/KondaShivaradhan/cloud/main/responce.json'
        resp = requests.get(url)
        data = json.loads(resp.text)
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
button.configure(command=button_click)
window.mainloop()
