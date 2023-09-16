from selenium.webdriver.common.by import By


class CompuHome ():
    
    location_input = (By.ID, "place-search-input") 
    select_position= (By.XPATH,"(//ul[@class='autocomplete']/li)")
    position_input = (By.ID, "prof-cat-search-input")
    search_button = (By.ID, "search-button")

class CompuVacancies():
    alert_button = (By.XPATH, "//button[contains(.,'Ahora no')]")
    option_date = (By.XPATH, "//p[contains(.,'Fecha')]")
    jobs = (By.XPATH, "(//a[@class='js-o-link fc_base'])")
    places = (By.XPATH, "(//p[@class='fs16 fc_base mt5 mb5'])")
    how_Long= (By.XPATH,"(//p[@class='fs13 fc_aux'])")

    @staticmethod
    def filt_date(filter_date):
        return(By.XPATH, "(//span[@class='buildLink '])["+filter_date+"]")
    