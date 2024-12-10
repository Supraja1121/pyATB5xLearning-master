class BaseTest:
    def open_Browser(self):
        print("Launching browser")

    def close_Browser(self):
        print("Closing Browser")

class TestCase(BaseTest):
    def testp(self):
        self.open_Browser()
        print("TCp executed")
        self.close_Browser()

    def testn(self):
        self.open_Browser()
        print("TCn executed")
        self.close_Browser()


class TestCase2(BaseTest):
    def test_2(self):
        self.open_Browser()
        print("TC2 executed")
        self.close_Browser()

a=BaseTest()
a.open_Browser()
a.close_Browser()