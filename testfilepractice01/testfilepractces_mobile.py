
import subprocess
import time
from datetime import datetime
from uiautomator import Device
d = Device("55fc7c16")
def videoStart(self,filename):
    global TS1
    global rec
    TS = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.mp4')
    TS1 = filename + TS
    command = ['adb', 'shell', 'screenrecord', '//Files/' + TS1]

    rec = subprocess.Popen(command)

    print("video recording started")

def videoStop(self, d_path):
        rec.terminate()
        time.sleep(2)
        cmd = ['adb', 'pull', 'Files/' + TS1, f'{d_path}']
        subprocess.run(cmd)
        print("video captured")

videoStart(0,"demo.mp4")
videoStop(0,"Files")
