#this is ui automator librarary
# #in librarymobile directory .here we are declaring uiautomator keywords


from uiautomator import Device
import time
import subprocess
d = Device("KJRKLNDAYLEYVO8T")
class Uilibrary():
    def __int__(self):
        #self.d = Device("KJRKLNDAYLEYVO8T")
        pass
    def clickBytext(self,textName):
        d(text=textName).click()
    def clickByicon(self,speed):
        d(text=speed).click()
    def backhome(self):
        # result page to back option
        d.click(65,130)


    # opening the history module
    def clickbyhistory(self):
        d.click(950,1650)
        print("opening histroy")
    def clicksinglehistory(self):
        d.click(1000,550)
        print("single history")
        time.sleep(2)
    def clickbydelete(self):
        d.click(870,130)
        print("pressing delte button ")
    def clickyesbutton(self,yname):
        d(text=yname).click()
        print("delete successfully")
    def clickbybacktostart(self):
        d.click(140, 1620)
    def clickthreelines(self):
        d.click(70,130)
    def clicksend(self,sendname):
        d(text=sendname).click()

    def sendmail(self,mailname):
        d(text=mailname).click()

    def clickremove(self):
        d.click(500,700)
    def clickmailsending(self):
        subprocess.run("adb shell input text pulipavangoud97@gmail.com", shell=True)  # here not getting

    def mailsending(self):
        d.click(900,100)
    def pressBack(self):
        d.press.back()


