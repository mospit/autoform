from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "chromedriver.exe"

def autofill(first_name, last_name,_phone, _email, _street1, _street2, _city, _state,_zip, _dob, _ssn):
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.listyourself.net/ListYourself/listing.jsp")

    FirstName = first_name
    LastName = last_name
    phone = _phone
    email = _email
    street = _street1
    street2 = _street2
    city = _city
    state = _state
    zip = _zip
    dob = _dob
    ssn = _ssn

    fNameSelector = driver.find_element_by_name("F_LSTGN")
    lNameSelector = driver.find_element_by_name("F_LSTNM")
    phoneSelector = driver.find_element_by_name("F_TELNO")
    emailSelector = driver.find_element_by_name("F_EMAIL")
    streetSelector = driver.find_element_by_name("F_STRT")
    citySelector = driver.find_element_by_name("F_LOCNM")
    stateSelector = driver.find_element_by_name("F_STATE")
    zipSelector = driver.find_element_by_name("F_ZIP")
    cEmailSelector = driver.find_element_by_name("EMAIL_CONFIRM")
    requireConfirmEmail = True

    fNameSelector.send_keys(FirstName)
    lNameSelector.send_keys(LastName)
    phoneSelector.send_keys(phone)
    emailSelector.send_keys(email)
    cEmailSelector.send_keys(email)
    streetSelector.send_keys(street)
    citySelector.send_keys(city)
    stateSelector.send_keys(state)
    zipSelector.send_keys(zip)

    
