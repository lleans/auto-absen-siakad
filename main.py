import scriptabsen
import values
import pytz
from time import time, sleep
from datetime import datetime

print("Ready")

while True:
    sleep(5 - time() % 5)

    WIB = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(WIB)

    if (time_now.strftime('%H') == '05' and
            time_now.strftime('%M') == '58' and
            time_now.strftime('%a') != 'Sat' and
            time_now.strftime('%a') != 'Sun'):
        temp = scriptabsen.runscript(values.email(), values.password(), values.browser())
        times = datetime.now(WIB)
        if(temp == True):
            print("Absen berhasil pada " + times.strftime('%c'))
        elif(temp == False):
            print("Absen gagal, SERVER SEKOLAH KENTANK, mencoba lagi " +
                  times.strftime('%c'))
            ass = scriptabsen.override(values.email(), values.password(), values.browser())
            if ass == True:
                timee = datetime.now(WIB)
                print("Absen berhasil pada " + timee.strftime('%c'))
        else:
            print("Server-mu Down " + times.strftime('%c'))