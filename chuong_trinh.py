# coding: utf-8
import os
import shutil
import time
import simplejson

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC


def dang_nhap_gmail(trinh_duyet, email, password):
    xpath_email = "//input[@id='identifierId']"
    xpath_pass = "//input[@name='password']"
    WebDriverWait(trinh_duyet, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_email))
    )
    time.sleep(3)
    email = trinh_duyet.find_element_by_xpath(xpath_email)
    email.send_keys(email_nguoi_dung)
    email.send_keys(Keys.ENTER)
    WebDriverWait(trinh_duyet, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath_pass))
    )
    password = trinh_duyet.find_element_by_xpath(xpath_pass)
    password.send_keys(password_nguoi_dung)
    time.sleep(3)
    # password.send_keys(Keys.ENTER)
    AC(trinh_duyet).send_keys(Keys.ENTER).perform()
    time.sleep(3)

    #trinh_duyet.get('https://ads.google.com/')

def lay_cookies(trinh_duyet):
    cookies = trinh_duyet.get_cookies()
    print(len(cookies))
    text = simplejson.dumps(cookies, indent=4, sort_keys=True)
    print(type(text))
    with open('cookies.txt', 'w') as tep_cookies:
        tep_cookies.write(text)

def lay_profile(trinh_duyet):
    trinh_duyet.get('about:support')
    duong_dan_profile_moi_xpath = '//*[@id="profile-dir-box"]'
    duong_dan_profile_moi = trinh_duyet.find_element_by_xpath(duong_dan_profile_moi_xpath).text
    print(duong_dan_profile_moi)
    noi_luu_profile_moi = os.path.join(thu_muc_cha, 'profile_moi')
    if os.path.exists(noi_luu_profile_moi):
        shutil.rmtree(noi_luu_profile_moi)
    shutil.copytree(
            duong_dan_profile_moi,
            noi_luu_profile_moi,
            ignore=shutil.ignore_patterns('*.lock'),
            )

def nen_thu_muc(duong_dan_thu_muc, duong_dan_luu):
    shutil.make_archive(
            duong_dan_thu_muc,
            "zip",
            duong_dan_luu,
            )

def thoat_trinh_duyet(trinh_duyet):
    trinh_duyet.quit()

if __name__ == '__main__':
    email_nguoi_dung = input("Nhap email: ")
    password_nguoi_dung = input("Nhap password: ")
    id_may_ao = input("Nhap id may ao: ")
    thu_muc_cha = os.path.abspath('..')
    duong_dan_fire_fox = os.path.join(
        thu_muc_cha,
        'FirefoxPortable',
        'App',
        'Firefox',
        'firefox.exe',
    )
    duong_dan_profile = os.path.join(
        thu_muc_cha,
        'FirefoxPortable',
        'Data',
        'profile',
        # 'profile_moi',
    )
    duong_dan_gecko = os.path.join(
        os.getcwd(),
        'geckodriver-v0.29.0-win64',
        'geckodriver.exe',
    )
    profile = FirefoxProfile(
            duong_dan_profile,
            )
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.set_preference("browser.tabs.remote.autostart", False)
    profile.set_preference("browser.tabs.remote.autostart.1", False)
    profile.set_preference("browser.tabs.remote.autostart.2", False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    trinh_duyet = webdriver.Firefox(
        firefox_binary=duong_dan_fire_fox,
        firefox_profile=profile,
        executable_path=duong_dan_gecko,
        desired_capabilities=desired,
    )
    trinh_duyet.get('https://accounts.google.com')
    dang_nhap_gmail(trinh_duyet, email, password)
