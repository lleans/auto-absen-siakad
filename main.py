import values
import scriptabsen as script
import pytz
import time
from datetime import datetime

print("Ready")

while True:
    time.sleep(5)
    WIB = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(WIB)
    
    if time_now.strftime('%H:%M') == '05:58' and time_now.strftime('%a') != 'Sat' and time_now.strftime('%a') != 'Sun':
        try:
            temp = script.runscript(values.email, values.password, values.browser())
            times = datetime.now(WIB)
            if temp:
                print("Absen berhasil pada", times.strftime('%c'))
            else:
                print("Absen gagal, SERVER SEKOLAH KENTANK, mencoba lagi",
                    times.strftime('%c'))
                if script.override(values.email, values.password, values.browser()) == True:
                    print("Absen berhasil pada", datetime.now(WIB).strftime('%c'))
        except:
            print("Server-mu Down", datetime.now(WIB).strftime('%c'))
