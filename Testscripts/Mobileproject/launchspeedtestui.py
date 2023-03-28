from Lamdaautomation.Utiles import speedtest
import time

objst = speedtest.speedtestUi()

objst.launchSpeedTestUi()
objst.startupanddown()
objst.backhomescreen()
time.sleep(2)
objst.clickhistory()
time.sleep(2)
objst.clicksinglehis()
objst.clickdelete()
time.sleep(2)
objst.clickyes()
time.sleep(3)
objst.clickbystarsp()
time.sleep(2)
objst.clickthreeliness()
time.sleep(2)
objst.clicksendfd()
time.sleep(2)
objst.clicksmail()
time.sleep(2)
objst.clickremovv()

time.sleep(2)
objst.mailsendingclick()
time.sleep(2)
objst.clickmailsending()
time.sleep(2)
for i in range(5):
    objst.pressBackUi()

