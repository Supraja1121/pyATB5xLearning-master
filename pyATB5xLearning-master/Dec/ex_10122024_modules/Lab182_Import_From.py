from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import close_browser


def test_Case():
    start_browser()
    print("Running TC")
    close_browser()

test_Case()