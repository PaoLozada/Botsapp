from selenium.webdriver.common.by import By

class YtbHome:
    search_box = (By.XPATH,"//input[@name='search_query']")
    name_video = (By.XPATH,"//yt-formatted-string[@class='style-scope ytd-video-renderer']")
    pop_up = (By.XPATH, "//button//span[contains(text(),'Aceptar')]")
    
class YtbVideo:
    views = (By.XPATH, "//span[contains(@class,'view-count')]")
    
   
    
    