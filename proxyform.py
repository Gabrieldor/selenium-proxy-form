from seleniumwire.undetected_chromedriver import Chrome
from faker import Faker
from selenium.webdriver.common.keys import Keys
import random
import time
import datetime
import os
import urllib
import pydub
import speech_recognition as sr

def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height


def scrap():

    username = 'YOUR_PROXY_USERNAME'
    password = 'YOUR_PROXY_PASSWORD'
    port = 22225
    random.seed(datetime.datetime.now())
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' % (username, session_id, password, port))

    lum_proxy = dict(http=super_proxy_url,https=super_proxy_url)

    options = {
        'proxy': lum_proxy
        }


    b = Chrome()
    b.get('https://www.ebay.co.uk/signin')
    input()
    e_input = b.find_element_by_id('email')
    pass_input = b.find_element_by_id('password-input-field')
    c_name_input = b.find_element_by_id('companyName')
    f_n_input = b.find_element_by_id('firstName')
    l_n_input = b.find_element_by_id('lastName')
    phone_input = b.find_element_by_id('proPhone')
    a_name_input = b.find_element_by_id('proAddress')
    z_code = b.find_element_by_id('proZipCode')
    dropdown = b.find_element_by_class_name("drop-down__select")
    btn_input = b.find_element_by_css_selector("button[type='submit']")

    fake = Faker('en-US')

    e_input.send_keys('YOUR_EMAIL')
    pass_input.send_keys('YOUR_PASSWORD')
    names = fake.name().split(' ')
    c_name_input.send_keys(fake.company())
    f_n_input.send_keys(names[0])
    l_n_input.send_keys(names[1])
    random_phone = str(random.randint(2030000000, 2039999999))
    phone_input.send_keys(random_phone)
    a_name_input.send_keys(fake.address())
    z_code.send_keys(fake.postcode())
    dropdown.find_elements_by_css_selector('option')[1].click()
    scroll_down(b)

    input()
    
    btn_input.click()
    #b.close()
    #scrap()

scrap()



