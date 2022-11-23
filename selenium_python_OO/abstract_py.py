from abc import ABC, abstractmethod

'''

Para uma classe se tornar abstrata precisamos imprtat o ABC e incluir a anotacao no metodo
'''


class Webdriver(ABC):

    @abstractmethod
    def click(self):  # método sem definição é um método abstrato
        pass


# obj = Webdriver()
# obj.click() #Can't instantiate abstract class Webdriver with abstract method click


class ChromeDriver(Webdriver):

    def capturingScreenshot(self):
        print('Capturing screenshot')

    def click(self):  # overriding
        print('Clicking in Chrome')


class FirefoxBrowser(Webdriver):

    def capturingScreenshot(self):
        print('Capturing screenshot')

    def click(self):  # overriding
        print('Clicking in Firefox')


obj = ChromeDriver()
obj.capturingScreenshot()
obj.click()

obj2 = FirefoxBrowser()
obj2.capturingScreenshot()

obj2.click()
