import time
from selenium import webdriver
import pytz
import datetime


def runscript(email, password, browser):
    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id")
    except:
        browser.close()
        return False

    emailinput = browser.find_element_by_class_name('email')
    passinput = browser.find_element_by_class_name('password')
    enter = browser.find_element_by_id('masuk')

    emailinput.send_keys(str(email))
    passinput.send_keys(str(password))
    enter.click()

    time.sleep(2)

    browser.get("https://siswa.smktelkom-mlg.sch.id/presnow")

    WIB = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(WIB)

    while(time_now.strftime('%H') == '06' and
          time_now.strftimr('%M') == '00'):
        browser.refresh()
        temp = browser.find_element_by_class_name('number')
        if(temp.text == 'Masuk'):
            browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
            browser.close()
            return True
        else:
            inputabsen = browser.find_element_by_xpath(
                "//section[2]/div[2]/div[2]/form/div/div[2]/div[1]/label[1]")
            simpan = browser.find_element_by_id("simpan")
            inputabsen.click()
            simpan.click()

            browser.refresh()
            tmp = browser.find_element_by_class_name('number')
            if(tmp.text == 'Masuk'):
                browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
                browser.close()
                return True
            else:
                browser.close()
                return False
