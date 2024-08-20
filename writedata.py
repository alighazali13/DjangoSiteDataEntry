from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import getpass


def go_to_safe_place(excel_file_name, res):

    browser = webdriver.Firefox()
    print("Browser opened.\n\n")
    browser.get('https://topschneider.ir/admin/')
    print("Page has been transferred.\n\n")

    # username_value = getpass.getpass("username : \n")
    # password_value = getpass.getpass("password : \n")

    print("Trying to login ...\n")
    username = browser.find_element(By.NAME, "username")
    username.send_keys('yuji13itadori')

    password = browser.find_element(By.NAME, "password")
    password.send_keys('Ac@56432')

    submit_button = browser.find_element(By.XPATH, "//form[@id='login-form']/div[3]/input")
    submit_button.click()

    feature_a = browser.find_element(By.LINK_TEXT, "Features")
    # print(feature_a.get_attribute('href'))
    feature_a.click()

    add_feature_parent = browser.find_element(By.CLASS_NAME, "object-tools")
    add_feature_a = add_feature_parent.find_element(By.CSS_SELECTOR,"a.addlink")
    # print(feature_a.get_attribute('href'))
    add_feature_a.click()


    for key, value in res.items():
        print("Trying to add " + key + " feature... ")
        product_selectbox = Select(browser.find_element(By.ID, "id_Product"))
        product_selectbox.select_by_visible_text(excel_file_name)

        featuretype_selectbox = Select(browser.find_element(By.ID, "id_FeatureType"))
        featuretype_selectbox.select_by_visible_text(value[1])

        feature_box = browser.find_element(By.ID, "id_feature")
        feature_box.send_keys(key)

        description_box = browser.find_element(By.ID, "id_descriptions")
        description_box.send_keys(value[0])
        if str(value[2]) == 'T':
            browser.find_element(By.ID, "id_important").click()
        saveandanother_parent = browser.find_element(By.CLASS_NAME, "submit-row")
        saveandanother_btn = saveandanother_parent.find_element(By.XPATH, "//input[2]")
        saveandanother_btn.click()
        print( key + " Done. ")

    time.sleep(20)

    browser.quit()


    

