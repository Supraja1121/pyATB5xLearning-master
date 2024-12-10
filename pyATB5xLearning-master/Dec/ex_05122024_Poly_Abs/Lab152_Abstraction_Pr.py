from abc import ABC, abstractmethod
class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass
    @abstractmethod
    def stopBrowser(self):
        pass

class Hidden(Browser):
    @abstractmethod
    def hidden(self):
        print("Hidden")

class TC1(Browser):
    def startBrowser(self):
        print("starting")

    def stopBrowser(self):
        print("stopping")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1 = TC1()
tc1.runTC()