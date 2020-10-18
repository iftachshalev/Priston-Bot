from win32gui import GetWindowText, GetForegroundWindow
from time import sleep

while True:
    sleep(0.5)
    print(GetWindowText(GetForegroundWindow()))
    if GetWindowText(GetForegroundWindow()) == "ThoughtsAndStreams – try.py PyCharm":
        print(1)
