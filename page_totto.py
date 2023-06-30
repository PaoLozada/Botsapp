from selenium.webdriver.common.by import By


class TottoHome ():
    menu_on = (By.ID, 'menu_on')
    close_adv = (By.XPATH, "//div[@class='bton-cerrar']/span")
    product_info = (By.XPATH, "//div[@class='_product-info']/h3/span[1]")

    @staticmethod
    def item_select(item):
        return (By.XPATH, "//li[@class='level2']["+item+"]")
    
    @staticmethod
    def filter_category(category):
        return (By.XPATH, "(//h5[contains(.,'"+category+"')])[2]")
    
    @staticmethod
    def filter_option(fOption):
        return (By.XPATH, "//a[contains(.,'"+fOption+"')]")