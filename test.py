import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class react(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:3000/react-tutorial-solutions")
        self.driver.maximize_window()
        time.sleep(5)

    def test_add(self):
        driver = self.driver


        # reset
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
        print('Reset button is visable')
        time.sleep(2)
        driver.find_element('xpath',xPath).click()


        # test win
        time.sleep(2)
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
        print("win")


        # play again
        time.sleep(2)
        xPath = '/html/body/div/div/div[1]/div[2]/button'
        assert driver.find_element("xpath", xPath).is_displayed()
        print('play again button is visable')
        time.sleep(2)
        driver.find_element('xpath',xPath).click()


        # test draw
        time.sleep(2)
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
        print('draw')
        time.sleep(2)


        def tearDown(self) -> None:
            self.driver.close()


# if __name__ == '__main__':
a = react()
a.setUp()
a.test_add()
a.tearDown()