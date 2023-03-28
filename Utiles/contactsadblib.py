#this is utile directory .using adb we are developing script

from Lamdaautomation.Library import adblibrary
from Lamdaautomation.Resources.testdata import mydata
obj = adblibrary.adblibrary()

class contactLibrary():

    def __int__(self):
        pass

    def launchContact(self):
        print("contact pkname is : ", mydata["contactPkname"])
        print("settings pkname is :", mydata["settingsPkname"])
        #obj.launchApp("com.android.contacts/.activities.PeopleActivity")
        obj.launchApp(mydata["contactPkname"])
        obj.launchApp(mydata["settingsPkname"])

    def pressBack(self):
        obj.pressBack()








