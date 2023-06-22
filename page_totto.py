from selenium.webdriver.common.by import By


class TottoHome ():
    menu_on = (By.ID, 'menu_on')
    new_collection = (By.XPATH, "//a[contains(.,'Nueva colección')]")
    product_info = (By.XPATH, "//div[@class='_product-info']/h3/span[1]")

    @staticmethod
    def item_select(item):
        return (By.XPATH, "(//img[@class=' b-error'])["+item+"]")
    
    @staticmethod
    def filter_category(category):
        return (By.XPATH, "(//h5[contains(.,'"+category+"')])[2]")
    
    @staticmethod
    def filter_option(fOption):
        return (By.XPATH, "//a[contains(.,'"+fOption+"')]")