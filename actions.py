import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Actions:

    @staticmethod
    def open_url(driver, url):
        driver.get(url)

    @staticmethod
    def move_to_element(driver, selector):
        acciones = ActionChains(driver)
        elementMove = driver.find_element(*selector)
        acciones.move_to_element(elementMove).perform()
    
    @staticmethod
    def scroll_to(driver, x, y):
        driver.execute_script("window.scrollTo({}, {});".format(x, y))

    @staticmethod
    def set_window_position(driver, x, y):
        driver.set_window_position(x, y)

    @staticmethod
    def set_window_size(driver, width, height):
        driver.set_window_size(width, height)

    @staticmethod
    def click_element(driver, selector):
        element = driver.find_element(*selector)
        element.click()

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)

    @staticmethod
    def get_texts(driver, selector):
        element = driver.find_elements(*selector)
        return [elem.text for elem in element]
    
    @staticmethod
    def get_text(driver, selector):
        element = driver.find_element(*selector)
        return [element.text]
    @staticmethod
    def send_k(driver, selector,my_keys):
        element = driver.find_element(*selector)
        element.send_keys(my_keys)