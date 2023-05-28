from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json

mivariable =''
def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getBotSearchOffer(driver: webdriver.Chrome) -> str:
    driver.set_window_position(0, 0)
    driver.set_window_size(1280, 1024)
    print('ingresaaa')
    acciones = ActionChains(driver)
    driver.get("https://www.toolsqa.com/")
    das = driver.current_url
    print(das)
    # Realizar acciones en la página
   
    menu = driver.find_element(By.XPATH,"(//span[@class='bar-long'])[1]")
    menu.click()
    qa = driver.find_element(By.XPATH,"(//div[contains(.,'QA Practices')])[5]")
    acciones.move_to_element(qa).perform()
    testing = driver.find_element(By.XPATH,"(//a[@href='/software-testing/software-testing-tutorial/'])[3]")
    testing.click()

    caption = driver.find_element(By.XPATH,"(//h1[contains(@class,'title')])[1]")
    time.sleep(1)
    print(caption.text + 'holaaaaaaaaaaaa')
    mivariable=caption.text
    print('Exitoso')
    return(mivariable)


'''def getBotSearchOffer(driver: webdriver.Chrome)-> dict:
    driver.set_window_position(0, 0)
    driver.set_window_size(1280, 1024)
    data ={}
    acciones = ActionChains(driver)
    driver.get("https://www.exito.com/")
    time.sleep(5)
    menu = driver.find_element(By.ID,"category-menu")
    menu.click()
    time.sleep(8)
    celulares = driver.find_element(By.ID,"undefined-nivel2-Celulares y accesorios")
    acciones.move_to_element(celulares).perform()
    smarp = driver.find_element(By.ID,'Categorías-nivel2-Smartphones')
    smarp.click()
    time.sleep(8)
    order = driver.find_element(By.XPATH,'//span[@class="vtex-search-result-3-x-orderByText c-muted-2"]')   
    order.click()
    time.sleep(8)
    moreH = driver.find_element(By.XPATH,'//button[contains(.,"Descuento")]')
    moreH.click()
    time.sleep(10)
    referencia = []
    valor =[]

    for i in range(3) :
        valRef=str(i+1)
        valVal=str((i+1)*2)
        ref = driver.find_element(By.XPATH,"(//span[@class='vtex-product-summary-2-x-productBrandName'])["+valRef+"]")
        val = driver.find_element(By.XPATH,"(//span[contains(@class,'exito-vtex-components-4-x-currencyContainer')])["+valVal+"]")
        referencia.append(ref.text)
        valor.append(val.text)        
    data['Exito']=[referencia, valor]
    print(data)
    return(data)'''

'''def getBotSearchOffer(driver: webdriver.Chrome)-> str:
    driver.set_window_position(0, 0)
    driver.set_window_size(1280, 1024)
  
   
    driver.get("https://www.exito.com/")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(5)
    menu = driver.find_element(By.XPATH,"//span[contains(.,'Super ofertas')]")
    print(menu.text)

    return(menu.tex)'''

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
