from selenium.webdriver.common.by import By

class YtbHome:

    search_box = (By.XPATH,"//input[@name='search_query']")
    
class YtbVideo:
    views = (By.XPATH,"(//span[contains(@class,'style-scope yt-formatted-string')])[1]")
    
    @staticmethod
    def val_views(video_name):
        return (By.XPATH,"//yt-formatted-string[contains(@aria-label, '{}')]".format(video_name))
    
    