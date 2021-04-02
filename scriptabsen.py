import pytz
import time
from datetime import datetime


def runscript(email, password, browser):
    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id")
    except:
        browser.close()
        return False

    emailinput = browser.find_element_by_xpath(
        '//*[@id="form_login"]/div[2]/div/input')
    passinput = browser.find_element_by_xpath(
        '//*[@id="form_login"]/div[3]/div/input')
    enter = browser.find_element_by_id('masuk')

    emailinput.send_keys(str(email))
    passinput.send_keys(str(password))
    enter.click()

    time.sleep(2)

    browser.get("https://siswa.smktelkom-mlg.sch.id/presnow")

    while True:
        time_now = datetime.now(pytz.timezone('Asia/Jakarta'))
        if time_now.strftime('%H') == '06':
            if cek_absen(browser) == False:
                absen(browser)
                if cek_absen(browser) == True:
                    logout(browser)
                    return True
                else:
                    logout(browser)
                    return False
            else:
                logout(browser)
                return True


def absen(browser):
    inputabsen = browser.find_element_by_xpath(
        "/html/body/section[2]/div[2]/div[2]/form/div/div[2]/div[1]/label[1]")
    simpan = browser.find_element_by_id("simpan")
    inputabsen.click()
    simpan.click()


def cek_absen(browser):
    browser.refresh()
    tmp = browser.find_element_by_class_name('number')
    if(tmp.text == 'Masuk'):
        return True
    else:
        return False


def logout(browser):
    browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
    browser.close()


def override(email, password, browser):
    while True:
        if runscript(email, password, browser) == True:
            return True
