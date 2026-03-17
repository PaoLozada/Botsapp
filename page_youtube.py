from selenium.webdriver.common.by import By

class YtbHome:
    search_box = (By.XPATH,"//input[@name='search_query']")
    name_video = (By.XPATH,"//yt-formatted-string[@class='style-scope ytd-video-renderer']")
    
class YtbVideo:
    views = (By.XPATH,"(//span[contains(@class,'style-scope yt-formatted-string')])[1]")
    
   
    
    