import os
from selenium import webdriver
#
#
#
# Emailmu Si AKAD blyat
email = ""
#
#
#
# Passwordmu Si AKAD blyat
password = ""

def browser():
    chromes = webdriver.ChromeOptions()
    chromes.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chromes.add_argument("--headless")
    chromes.add_argument("--no-sandbox")
    chromes.add_argument("--disable-dev-sh-usage")

    browser = webdriver.Chrome(executable_path=os.environ.get(
        "CHROMEDRIVER_PATH"), chrome_options=chromes)
    
    return browser