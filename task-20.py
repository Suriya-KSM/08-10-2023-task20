from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class cowin:

    def __init__(self, web_url):
        self.url=web_url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(7)
            cowin_window=self.driver.window_handles[0]

            #Opening FAQ page in new window
            self.driver.find_element(by=By.LINK_TEXT, value='FAQ').click()
            sleep(5)
            FAQ_window_id=self.driver.window_handles[1]
            print("FAQ window ID: ", FAQ_window_id)

            #opening Partner page in new window
            self.driver.find_element(by=By.XPATH, value='/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
            sleep(5)
            Partner_window_id=self.driver.window_handles[2]
            print("\n\nPartner window ID: ",Partner_window_id)
            
            #closing the newly opened window
            N=self.driver.window_handles
            for i in N:
                if i != cowin_window:
                    self.driver.switch_to.window(i)
                    self.driver.close()
                    sleep(2)

            #switching back to the home window
            self.driver.switch_to.window(cowin_window)
            sleep(3)

        #exception handling
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        #and finally quitting the browser
        finally:
            self.driver.quit()


#declaring a variable which holds url of the website
URL = "https://www.cowin.gov.in/"

#creating obj the main class
obj=cowin(URL)

#calling the function inside the class using object
obj.login()

