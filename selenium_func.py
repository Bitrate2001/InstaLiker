import os
import zipfile
import shutil

from os.path import sep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver import Remote
from webdriverdownloader import GeckoDriverDownloader

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException


# Creating plugin for hide Selenium
def create_firefox_extension():
    ext_path = os.path.abspath(os.path.dirname(__file__) + sep + "firefox_extension")
    # safe into assets folder
    zip_file = "extension.xpi"

    files = ["manifest.json", "content.js", "arrive.js"]
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED, False) as zipf:
        for file in files:
            zipf.write(ext_path + sep + file, file)

    return zip_file


# Init a profile
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)

# Install hide selenium addon
driver.install_addon(create_firefox_extension(), temporary=True)


# Create the function for getting the desired link
def get_page(url):
    driver.get(url)


def close_window():
    driver.close()
