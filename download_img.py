import sys
import os
import time
import base64
import json
import math
import random
import numpy as np
import requests
from cv2 import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
#user_data_dir='--user-data-dir=C:/Users/chupa/AppData/Local/Google/Chrome/User Data/Default'
#crt_file=r'C:\Users\chupa\Downloads\Ghelper2.2.1.all\Ghelper2.2.1.crx'
#chrome_options.add_argument(user_data_dir)
#chrome_options.add_extension(crt_file)

#'permissions.default.stylesheet': 2,     
#'javascript': 2        
#'images': 2,
prefs = {
    'profile.default_content_setting_values': {

    }
}
chrome_options.add_experimental_option('prefs', prefs)
broswer=webdriver.Chrome(executable_path="E:/Program Files/Python/chromedriver.exe",options=chrome_options)
search_url=\
"https://image.baidu.com/search/detail?ct=503316480&z=2&ipn=d&word=%E7%A7%91%E6%AF%94%2024%E5%8F%B7%208%E5%8F%B7&step_word=&hs=0&pn=0&spn=0&di=55110&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2025599050%2C3147604196&os=32522279%2C3120023171&simid=3506657392%2C517023672&adpicid=0&lpn=0&ln=1085&fr=&fmq=1600795174169_R&fm=result&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=0&height=0&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fn.sinaimg.cn%2Fdl%2Ftransform%2F20170913%2FsnYC-fykusey9720794.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3F1s_z%26e3Bftgw_z%26e3Bv54_z%26e3BvgAzdH3FgjofAzdH3FojgptAzdH3Fda80-al-8nAzdH3F1jpwts-tuyh7fjyl0dc9ba_z%26e3Bfip4s&gsm=1&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
broswer.get(search_url)

# loading login page's captcha
img_path="./download_img/"
if os.access(img_path, os.F_OK) == False:
    os.mkdir(img_path)


for index in range(500):
    current_img=WebDriverWait(broswer, 60, 0.1).until(EC.visibility_of_element_located((By.ID, "currentImg")))
    img_url=current_img.get_attribute("src")
    requests_result = requests.get(img_url, stream=True)
    if requests_result.status_code == 200:
        open('./download_img/{:0>5d}.png'.format(index), 'wb').write(requests_result.content) 
        print(img_url)
        btn_next_img=WebDriverWait(broswer, 10, 0.1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='img-next'")))
        print(btn_next_img)
        btn_next_img.click()
        time.sleep(0.1)



