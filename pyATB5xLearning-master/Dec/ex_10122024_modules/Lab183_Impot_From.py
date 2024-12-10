from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import close_browser




class TestCase:
    def test_Case(self):
        start_browser()
        print("Running TC")
        close_browser()

tc=TestCase()
tc.test_Case()
