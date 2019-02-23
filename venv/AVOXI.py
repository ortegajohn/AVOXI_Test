
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotInteractableException
import time
import random



#use the firefox version 52.0.2 from https://ftp.mozilla.org/pub/firefox/releases/52.0.2/
#Download:   https://ftp.mozilla.org/pub/firefox/releases/52.0.2/firefox-52.0.2.win64.sdk.zip
driver = webdriver.Firefox(executable_path=r'selenium\\webdriver\\geckodriver.exe')


cardNumbers = ['370000000000002','6011000000000012','3088000000000017','38000000000006','4007000000027',
              '4012888818888','4111111111111111','5424000000000015','2223000010309703','2223000010309711']

cardCode = ['900','901','904','902','903']


# define repeatable events
def clickWid(id):
    variable1 = driver.find_element_by_id ( id )
    variable1.click ()


def clickWxpath(xpath):
    variable2 = driver.find_element_by_xpath ( xpath )
    variable2.click ()


def sendKeysWid(id, text):
    variable3 = driver.find_element_by_id ( id )
    variable3.send_keys ( text )

def thepopup():
    time.sleep ( 2 )
    clickWxpath('.//*[@id=\'continueShoppingPromoButton\']/div/div/a')


for j in cardCode:#try every combination of given card number and code
    for i in cardNumbers:#check every card number

        driver.get('https://shoppingcart-staging.avoxi.io/')


        time.sleep(7)#the page takes an inconsistent time to load
        clickWxpath('.//*[@id=\'numberType\']/select/option[26]')

        time.sleep(2)
        #Sometimes selecting a numberType does not result in an id=number being displayed
        try:
            clickWid('number')
            time.sleep(2)
            clickWxpath('.//*[@id=\'number\']/select/option[2]')
        except (TimeoutError,WebDriverException):
            pass

        try:
            # Clicking this twice seems to work
            clickWid('businessStandardButton')
            time.sleep(2)
            clickWid('businessStandardButton')
        except(ElementNotInteractableException):
            thepopup()

        #fill in fields
        sendKeysWid('firstName','firstName')
        sendKeysWid('lastName','lastName')
        sendKeysWid('businessName','businessName')
        sendKeysWid('email','a@mail.com')
        time.sleep(2)#button time to enable
        clickWid('newCustomerButton')#click continue
        sendKeysWid('billingName','billing Name')

        #use random item in cardNumbers list
        #sendKeysWid('billingCardNumber',cardNumbers[random.randint(0,len(cardNumbers)-1)])
        sendKeysWid ( 'billingCardNumber', i )


        sendKeysWid('billingExpMon','4')
        sendKeysWid('billingExpYear','2020')

        #use random item in cardCode list
        #sendKeysWid('billingCVC',cardCode[random.randint(0,len(cardCode)-1)])
        sendKeysWid ( 'billingCVC', j)
        clickWxpath('.//*[@id=\'content\']/div/div[1]/div[2]/div[4]/div[2]/div/div/div[2]/div/div/label')#checkbox
        clickWid('placeOrder')
        time.sleep(2)#wait for the page to load

        print(i)
        print(j)
        print('--------')
