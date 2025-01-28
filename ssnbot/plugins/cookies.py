import os
import json
from pyrogram import Client, filters
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CURRENT_SITE_URL = "https://www.youtube.com/"


GMAIL_ID = ""
GMAIL_PASSWORD = ""

COOKIES_FILE = "cookies.txt"


options = Options()
options.headless = True




def generate_cookies():
    driver = webdriver.Firefox(options=options)
    driver.get(CURRENT_SITE_URL)
    driver.find_element(By.NAME, "email").send_keys(GMAIL_ID)
    driver.find_element(By.NAME, "password").send_keys(GMAIL_PASSWORD)
    driver.find_element(By.ID, "identifierNext").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passwordNext")))
    driver.find_element(By.ID, "passwordNext").click()
    cookies = driver.get_cookies()
    with open(COOKIES_FILE, "w") as f:
        json.dump(cookies, f)
    driver.quit()

@app.on_message(filters.command("cookies"))
async def send_cookies(client, message):
    try:
        generate_cookies()
        await message.reply_document(COOKIES_FILE)
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")