import time
from selenium import webdriver

def runscript(email, password, browser):
    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id/welcome")
    except:
        browser.close()
        return False

    emailinput = browser.find_element_by_xpath(
        '//form[@id="form_login"]/div[2]/div[1]/input[1]')
    passinput = browser.find_element_by_xpath(
        '//form[@id="form_login"]/div[3]/div[1]/input[1]')
    enter = browser.find_element_by_xpath(
        '//form[@id="form_login"]/div[4]/div[1]/input[1]')

    emailinput.send_keys(str(email))
    passinput.send_keys(str(password))
    enter.click()

    time.sleep(1)

    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id/presnow")
    except:
        browser.close()
        return False

    time.sleep(2)
    temp = browser.find_element_by_class_name("number")
    if(temp.text == 'Masuk'):
        browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
        browser.close()
        return True
    else:
        inputabsen = browser.find_element_by_xpath(
            "//select[@id='ijin_pilih']/option[text()='Masuk']")
        simpan = browser.find_element_by_name("simpan")
        inputabsen.click()
        simpan.click()

        time.sleep(2)
        browser.refresh()
        tmp = browser.find_element_by_class_name("number")
        if(tmp.text == 'Masuk'):
            browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
            browser.close()
            return True
        else:
            browser.close()
            return False