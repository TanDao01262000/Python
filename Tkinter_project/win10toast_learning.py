"""An easy-to-use Python library for displaying Windows 10 Toast Notifications which is
 useful for Windows GUI development."""

import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == "18:10:30":
        print(current_time)
        toaster.show_toast(title="Notification", msg='Testing Notification', icon_path=None, duration=10)
        break


