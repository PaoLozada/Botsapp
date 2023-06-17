from selenium.webdriver.common.by import By

class KatroHome:

    cel = (By.XPATH,"(//a[@title='Celulares'])[1]")
    celu = (By.XPATH,"//a[@data-subcategory='Celulares']")
    notifi = (By.XPATH,"//button[@class='button-primary js-cookie-notification-accept']")
    
class KatroCell:
    order = (By.XPATH,"//div[@class='float-select js-float-select js-float-group full-width active-click']")
    menor = (By.XPATH,"//li[contains(.,'Precio: menor a mayor')]")

    @staticmethod
    def val_element(val):
        return (By.XPATH, "(//span[contains(@class,'price')])["+val+"]")
    
    @staticmethod
    def ref_element(ref):
        return (By.XPATH, "(//div[@class='product__item__information__brand'])["+ref+"]")