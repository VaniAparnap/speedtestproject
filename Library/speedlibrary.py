from uiautomator import Device
import time
#class newtestapp():
    #def test_installspeedapp(self):

#code for speed test opening the app
class uilibraryspeed():
    def __int__(self):
        d = Device("ZY223Q2R98")
        pass
    def clickbytext(self,appname):
        d(text="")



d(text="Speed Test").click()
time.sleep(3)

#here we are clicking start to know the mbpsof download and upload
d(text="Start").click()
time.sleep(10)
print("click start")

d.click(65,130)
print("going to start screen")
time.sleep(2)

#opening the history module

d(text="History").click()
print("opening histroy")
time.sleep(2)

d.click(1000, 550)
print("delete single history")
time.sleep(2)

d.click(850, 80)
time.sleep(2)
d(text="Yes").click()
print("delete successfully")

#for i in range(2):
    #d.press.back()