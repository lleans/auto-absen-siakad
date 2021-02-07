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

    if(time_now.strftime('%H') == '06' and
            time_now.strftime('%M') == '02' and
            time_now.strftime('%a') != 'Sat' and
            time_now.strftime('%a') != 'Sun'):
        temp = scriptabsen.runscript(values.email(), values.password(), values.browser())
        if(temp == True):
            print("Absen berhasil pada " + time_now.strftime('%c'))
            tmp = True;
        elif(temp == False):
            print("Absen gagal, SERVER SEKOLAH KENTANK " +
                  time_now.strftime('%c'))
        else:
            print("Server-mu Down " + time_now.strftime('%c'))