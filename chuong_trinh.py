# coding: utf-8
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


thu_muc_cha = os.path.abspath('..')
duong_dan_fire_fox = os.path.join(
    thu_muc_cha,
    'FirefoxPortable V15',
    'App',
    'Firefox',
    'firefox.exe',
)
duong_dan_fire_fox = r"C:\Program Files\Mozilla Firefox\firefox.exe"
duong_dan_profile = os.path.join(
    thu_muc_cha,
    'profile',
)
duong_dan_profile = r"C:\Users\DVKH\AppData\Roaming\Mozilla\Firefox\Profiles\vdlvrf7e.default-release-3"
duong_dan_gecko = os.path.join(
    os.getcwd(),
    'geckodriver-v0.29.0-win64',
    'geckodriver.exe',
)
# binary_firefox: FirefoxBinary = FirefoxBinary(duong_dan_fire_fox)
# binary_firefox.add_command_line_options('-allow-downgrade')
profile = FirefoxProfile()
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

trinh_duyet = webdriver.Firefox(
    firefox_binary=duong_dan_fire_fox,
    firefox_profile=profile,
    executable_path=duong_dan_gecko,
    desired_capabilities=desired,
)
trinh_duyet.get('https://accounts.google.com')
xpath_email = "//input[@id='identifierId']"
xpath_pass = "//input[@name='password']"
WebDriverWait(trinh_duyet, 20).until(
    EC.element_to_be_clickable((By.XPATH, xpath_email))
)
email = trinh_duyet.find_element_by_xpath(xpath_email)
email.send_keys('htuananh14061')
email.send_keys(Keys.ENTER)
WebDriverWait(trinh_duyet, 20).until(
    EC.element_to_be_clickable((By.XPATH, xpath_pass))
)
password = trinh_duyet.find_element_by_xpath(xpath_pass)
password.send_keys('1234')
password.send_keys(Keys.ENTER)

time.sleep(5)
trinh_duyet.get('https://ads.google.com/')
cookies = trinh_duyet.get_cookies()
print(cookies)
with open('cookies.txt', 'w') as tep_cookies:
    pickle.dump(cookies, tep_cookies)