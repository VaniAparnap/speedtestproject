#this is utile directory .using uiautomation we are developing script
from Lamdaautomation.Library import Uiaulibrary

obj = Uiaulibrary.Uilibrary()

class contactLibraryUi():

    def __int__(self):
        pass


    def launchContactUi(self):
        obj.clickBytext("Contacts")  #here we are creating object for uilibrary methoods

    def pressBackUi(self):
        obj.pressBack()  #here we are creating object for uilibrary methoods

