#this is testscript directory .here we are importing contactuilib and creating object to the class
#

from Lamdaautomation.Utiles import contactsuilib
import time

obj = contactsuilib.contactLibraryUi()

obj.launchContactUi()
time.sleep(2)
obj.pressBackUi()