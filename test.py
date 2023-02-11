
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import warnings


class react(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:3000/react-tutorial-solutions")
        time.sleep(5)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


    def testReset(self):
        driver = self.driver
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[1]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[1]'
        driver.find_element('xpath',xPath).click()

        xPath = '/html/body/div/div/div[1]/div[2]/button'
        assert "Reset game" in driver.find_element("xpath", xPath).text
        assert driver.find_element("xpath", xPath).is_displayed()
        print('Reset button is visible')
        time.sleep(2)
        driver.find_element('xpath',xPath).click()

    def testWin(self):
        driver = self.driver
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[3]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[2]'
        driver.find_element('xpath',xPath).click()

        xPath = '//*[@id="root"]/div/div[1]/div[2]/h2'
        assert "\"X\" is winner!" in driver.find_element("xpath", xPath).text
        print("Displayed winner text")
        time.sleep(2)

    def testPlayAgain(self):
        driver = self.driver
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[3]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[2]/button'

        assert driver.find_element("xpath", xPath).is_displayed()
        print('Play again button is visible')
        time.sleep(2)
        driver.find_element('xpath',xPath).click()

    def testDraw(self):
        driver = self.driver
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[1]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[1]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[3]/button[1]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[3]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[3]/button[2]'
        driver.find_element('xpath',xPath).click()

        xPath = '/html/body/div/div/div[1]/h2'
        assert "Draw!" in driver.find_element("xpath", xPath).text
        print('Displayed draw text')
        time.sleep(2)

    def testMidGame(self):
        driver = self.driver
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[1]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[2]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[1]/button[3]'
        driver.find_element('xpath',xPath).click()
        xPath = '/html/body/div/div/div[1]/div[1]/div/div[2]/button[1]'
        driver.find_element('xpath',xPath).click()

        xPath = "/html/body/div/div/div[2]/ol/li[5]/button"
        assert driver.find_element("xpath", xPath).is_displayed()
        print('correct move button is visible')
        time.sleep(2)
        driver.find_element('xpath',xPath).click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':    
    unittest.main()