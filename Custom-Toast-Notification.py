import time
from win10toast import ToastNotifier

notify = ToastNotifier()

notify.show_toast("Python", "Hello World!", duration=10)

time.sleep(10)
