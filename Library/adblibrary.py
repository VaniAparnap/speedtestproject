#in librarymobile directory .here we are declaring adb keywords

import subprocess

class adblibrary():
    def __int__(self):
        subprocess.check_output("adb devices")
        # print("device connected")
        pass
    def launchApp(self,apkname):
        subprocess.run(['adb', 'shell', 'am', 'start', '-n', apkname])
        print("apk started sucessfully")


    def pressBack(self):
        subprocess.run("adb shell input keyevent 4")



