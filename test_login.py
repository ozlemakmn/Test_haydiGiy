from userinfo import username ,password,username1,password1,password2,name,lastname,eposta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from constants.globalconstants import *
import pytest


class Test_Login:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        
        
    def teardown_method(self):
        self.driver.quit()  
        
    def test_login(self): 
        
       logo=self.waitForElementVisible((By.CSS_SELECTOR,"body > div.header > div.header-main > div > div.header-logo > a > img"))
       assert logo.is_displayed(), "Logo görüntülenmiyor." #logonun görünlendiğini kontrol etmek için kullanılır.                               
       
       tabs = self.driver.find_elements(By.CSS_SELECTOR, "div-header-menu-container ul li a") #birden fazla tab menü olduğu için find_elements locater'ını kullandım.
       expected_menu = ["YENİ GELENLER","İNDİRİMLİ ÜRÜNLER","ÇOK SATANLAR","SERİ SONU","ÜST GİYİM","ALT GİYİM","EŞOFMAN - PİJAMA","ELBİSE-TULUM","ÇOCUK-BEBEK","AYAKKABI","AKSESUAR","İÇ GİYİM","ERKEK"]  # Beklenen tab menü isimleri

     # Her bir tab menü ismini kontrol ettir.
       for i, tab in enumerate(tabs): #enumarete  elemanın hem kendisine hemde indeks numarasına aynı anda erişim sağlamak için kullanılır.
        assert tab.text == expected_menu[i], f"Sekme ismi beklenen ile uyuşmuyor: {tab.text}"
            
        
       üyeolButton = self.waitForElementVisible((By.XPATH,üyeolButton_id))
       üyeolButton.click()
       usernameInput= self.waitForElementVisible((By.ID,usernameInput_id))
       passwordInput= self.waitForElementVisible((By.ID,passwordInput_id))
       actions = ActionChains(self.driver)
       actions.send_keys_to_element(usernameInput,username )
       actions.send_keys_to_element(passwordInput, password)
       actions.perform()  #ilgili aksiyonları çalıştır.
       singIn = self.waitForElementVisible((By.XPATH,singIn_id))
       singIn.click()
       logoButton=self.waitForElementVisible((By.XPATH,logoButton_id))
       logoButton.click()
       searchInput=self.waitForElementVisible((By.NAME,searchInput_id))
       searchInput.send_keys("çanta", Keys.ENTER)
       firstclass=self.waitForElementVisible((By.XPATH, firstclass_id))
       firstclass.click()
       
       basket=self.waitForElementVisible((By.ID,basket_id))
       basket.click()
       #assert self.driver.find_element((By.CSS_SELECTOR, ".toast-title")).text == addedtoyourcart
       
       tocartadd=self.waitForElementVisible((By.XPATH,tocartadd_id))
       tocartadd.click()                                        
                                                 
    def waitForElementVisible(self,locator,timeout=5):
     return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))    
    @pytest.mark.skip
    def test_invalidlogin(self): 
       login_button = self.waitForElementVisible((By.XPATH, login_button_id))
       login_button.click()
       usernameInput= self.waitForElementVisible((By.ID,usernameInput_id))
       
       passwordInput= self.waitForElementVisible((By.ID,passwordInput_id))
       actions = ActionChains(self.driver)
       actions.send_keys_to_element(usernameInput, username1)
       actions.send_keys_to_element(passwordInput, password1)
       actions.perform()  

       singIn = self.waitForElementVisible((By.XPATH,singIn_id))
       singIn.click()
       errorMessage= self.waitForElementVisible((By.XPATH,errorMessage_id ))
       assert errorMessage.text == error_message_text
    @pytest.mark.skip
    def test_signup(self): 
       login_button = self.waitForElementVisible((By.XPATH,login_button_id ))
       login_button.click()
       signup_button = self.waitForElementVisible((By.XPATH,signup_button_id))
       signup_button.click()
       nameInput= self.waitForElementVisible((By.ID,nameInput_id))
       lastnameInput= self.waitForElementVisible((By.ID,lastnameInput_id))
       epostaInput= self.waitForElementVisible((By.ID,usernameInput_id))
       passwordInput= self.waitForElementVisible((By.ID,passwordInput_id))
       
       actions = ActionChains(self.driver)
       actions.send_keys_to_element(nameInput, name)
       actions.send_keys_to_element(lastnameInput,lastname)
       actions.send_keys_to_element(epostaInput,eposta)
       actions.send_keys_to_element(passwordInput, password2)
       actions.perform()  
       
       sing_up = self.waitForElementVisible((By.ID,sing_up_id))
       sing_up.click()
     
       successfulmessage = self.waitForElementVisible((By.XPATH, successfulmessage_id))
       assert successfulmessage.text == successful_message_text
         
