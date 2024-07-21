import time
import os
from playsound import playsound

clear = lambda: os.system('cls')

work = 1500
long_break = 900
short_break = 300

counter = 0

def countdown(seconds):
    clear()
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print('{:02d}:{:02d}:{:02d}'.format(hours, mins, secs), end='\r')
        time.sleep(1)
        seconds -= 1
    playsound('kakao.mp3')

def main():
    clear()
    global counter
    input('press any key to start work timer')
    countdown(work)
    input('press any key to start break timer')
    if counter < 3:
        countdown(short_break)
        counter += 1
    else:
        countdown(long_break)
        counter = 0
    main()

main()
