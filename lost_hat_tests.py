import unittest
from selenium import webdriver

from helpers import funcional_helpers as fh


class LostHatTests(unittest.TestCase):


    def setUp(self):
        #self.driver =   webdriver.Chrome(executable_path='C:\TestFile\chromedriver.exe')
        #driver = self.driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.url_login = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.url_product = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'




    def tearDown(self):
        self.driver.quit()



    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

           :param driver: webdriver instance
           :param xpath: xpath to element with text to be observed
           :param expected_text: text what we expecting to be found
           :return: None
        """
        header_element = driver.find_element_by_xpath(xpath)
        header_element_text = header_element.text
        print(header_element_text)
        self.assertEqual(expected_text, header_element_text, f'Expected text differ from actual od page: {driver.current_url}')

#sprawdzenie czy nagłówek ‘Log in to your account’ występuje na stronie logowania,
    def test_login_header(self):
        driver = self.driver
        driver.get(self.url_login)
        expected_text = 'Log in to your account'
        xpath = '//*[@id="main"]/header'
        self.assert_element_text(driver, xpath, expected_text)


#bledne logowanie
    def test_incorrect_login(self):
        user_email = 'bartek@test.pl'
        user_password = '12345'
        expected_text = 'Authentication failed.'
        xpath = '//*[@class="alert alert-danger"]'
        driver = self.driver
        driver.get(self.url_login)
        fh.user_login(driver, user_email, user_password)
        self.assert_element_text(driver, xpath, expected_text)



#sprawdzenie czy możliwe jest zalogowanie się na stronie
    def test_correct_login(self):
        user_email = 'tester@test.pl'
        user_password = '12345678'
        expected_text = 'Your account'
        xpath = '//*[@id="main"]/header/h1'
        driver = self.driver
        driver.get(self.url_login)
        fh.user_login(driver, user_email, user_password)
        self.assert_element_text(driver, xpath, expected_text)


#sprawdzenie czy produkt posiada poprawną nazwę HUMMINGBIRD PRINTED T-SHIRT oraz aktualną cenę PLN23.52
    def test_name_product(self):
        driver = self.driver
        driver.get(self.url_product)
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        xpath = '//*[@id="main"]/div[1]/div[2]/h1'
        #t_shirt_name
        self.assert_element_text(driver, xpath , expected_text)

        #price
    def test_price_product(self):
        driver = self.driver
        driver.get(self.url_product)
        expected_text = 'PLN23.52'
        xpath = '//*[@class="current-price"]/span'
        self.assert_element_text(driver, xpath, expected_text)



if __name__ == '__main__':
    unittest.main(unittest.TestCase)
