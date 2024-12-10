class OldBrowser:
    def bs(self):
        print("IE start")

    def be(self):
        print("IE end")

class NewBrowser(OldBrowser):
    def bs(self):
        super().bs()
        print("Chrome start")

    def be(self):
        super().be()
        print("Chrome end")

ob=OldBrowser()
nb=NewBrowser()
nb.bs()
nb.be()