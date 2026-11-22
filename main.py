import time
from datetime import datetime
from pynput.keyboard import Controller, Key
import pyautogui
import webbrowser

keyboard = Controller()

isStarted = False

lst = [
    ["https://us06web.zoom.us/j/87998146955?pwd=aVdEa773B4iRQheu2qCoIWr6Uf40Vp.1","12:05","13:05"],
    ["https://us05web.zoom.us/j/81713078992?pwd=mFWHJfSCixKYJNfp12JRuxwcVGZs3b.1","15:10","16:20"]
]

for i in lst:
    meeting_link = i[0]
    start_time = i[1]
    end_time = i[2]

    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    while True:
        now = datetime.now()

        if not isStarted:
            if now.hour == start_hour and now.minute == start_minute:
                webbrowser.open(meeting_link)
                print("Joined Success")

                # Wait for Zoom to open/join
                time.sleep(500)

                # Check that zoom is active and working
                
                pyautogui.click(x=1137, y=550)
                
                print("clicked once")

                time.sleep(3)
                pyautogui.click(x=1137, y=550)
                
                print("clicked Twice")

                # Open Zoom chat: Alt + H
                keyboard.press(Key.alt_l)
                keyboard.press('h')
                time.sleep(0.2)
                keyboard.release('h')
                keyboard.release(Key.alt_l)
                print("Opened Chat Box")
                time.sleep(1)

                # Type message in chat
                keyboard.type("Siddharth present")

                # Send message
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                print("Attendance Done")
                isStarted = True

        else:
            if now.hour == end_hour and now.minute == end_minute:
                # Leave meeting: Alt + Q
                keyboard.press(Key.alt_l)
                keyboard.press('q')
                time.sleep(0.1)
                keyboard.release('q')
                keyboard.release(Key.alt_l)

                time.sleep(1)

                # Confirm leave meeting
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

                isStarted = False
                break

        time.sleep(5)