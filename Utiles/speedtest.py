from Lamdaautomation.Library import Uiaulibrary

import time
objst = Uiaulibrary.Uilibrary()
class speedtestUi():
    def __int__(self):
        pass

    def launchSpeedTestUi(self):
        objst.clickBytext("Speed Test")  #here we are creating object for uilibrary methoods


    def startupanddown(self):
        objst.clickByicon("Start")
        # here we are clicking start to know the mbpsof download and upload

        time.sleep(15)
        print("click start")

    def backhomescreen(self):
        objst.backhome()
    def clickhistory(self):
        objst.clickbyhistory()
    def clicksinglehis(self):
        objst.clicksinglehistory()
    def clickdelete(self):
        objst.clickbydelete()
    def clickyes(self):
        objst.clickyesbutton("Yes")
    def clickbystarsp(self):
        objst.clickbybacktostart()
    def clickthreeliness(self):
        objst.clickthreelines()
    def clicksendfd(self):
        objst.clicksend("Send feedback")
    def clicksmail(self):
        objst.sendmail("speedtest@app.ecomobile.vn")
        objst.sendmail("speedtest@app.ecomobile.vn")
    def clickremovv(self):
        objst.clickremove()
    def mailsendingclick(self):
        objst.clickmailsending()

    def clickmailsending(self):
        objst.mailsending()
    def pressBackUi(self):
        objst.pressBack()

