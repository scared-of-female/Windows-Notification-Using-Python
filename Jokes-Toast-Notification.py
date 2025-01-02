import pyjokes
import time
from win10toast import ToastNotifier

notify = ToastNotifier()

joke = pyjokes.get_joke()

notify.show_toast("Time to laugh!", joke, duration=10)

time.sleep(10)
