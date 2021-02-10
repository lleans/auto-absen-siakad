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
    enter = browser.find_element_by_id(
        'masuk')

    emailinput.send_keys(str(email))
    passinput.send_keys(str(password))
    enter.click()

    time.sleep(2)

    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id/presnow")
    except:
        browser.close()
        return False

    time.sleep(1)
    temp = browser.find_element_by_xpath("//section[2]/div[2]/div/div/div[2]/div[2]")
    if(temp.text == 'Masuk'):
        browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
        browser.close()
        return True
    else:
        inputabsen = browser.find_element_by_xpath("//section[2]/div[2]/div[2]/form/div/div[2]/div[1]/label[1]")
        simpan = browser.find_element_by_id("simpan")
        inputabsen.click()
        simpan.click()

        browser.refresh()
        tmp = browser.find_element_by_xpath("//section[2]/div[2]/div/div/div[2]/div[2]")
        if(tmp.text == 'Masuk'):
            browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
            browser.close()
            return True
        else:
            browser.close()
            return False
