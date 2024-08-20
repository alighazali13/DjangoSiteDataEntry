from selenium import webdriver
from selenium.webdriver.common.by import By



def start_scrapping_det(DetLink):

    browser = webdriver.Firefox()
    print("Browser opened.\n\n")
    browser.get(DetLink)
    print("Page has been transferred.\n\n")

    
    # html_brandName = browser.find_element(By.CLASS_NAME, "product-manufacturer")
    # brandName = browser.find_element(By.TAG_NAME, 'h1')
    # print(brandName.text)

    print("Trying to get product details from the site ...\n")

    

# dont remove below codes, this is a good idea ;
    # THEADS = []
    # TBODIES = []

    # table_parent = browser.find_element(By.CLASS_NAME, "table-responsive")
    # # thead 
    # thead_contents = table_parent.find_elements(By.TAG_NAME, "thead")
    # for thead_content in thead_contents:
    #     THEADS.append(thead_content.get_attribute("outerHTML"))
    # # aaa = fff.get_attribute("outerHTML")
    # # print(THEADS)
    # print('THEADS - - - -- - -- - - -- -  -\n')


    # # tbody 
    # tbody_contents = table_parent.find_elements(By.TAG_NAME, "tbody")
    # for tbody_content in tbody_contents:
    #     TBODIES.append(tbody_content.get_attribute("outerHTML"))
    # # aaa = fff.get_attribute("outerHTML")
    # # print(TBODIES)
    # print('TBODIES - - - -- - -- - - -- -  -\n')

    # # THEADS = ['<thead><tr><td colspan="2"><strong>فنی</strong></td></tr></thead>', '<thead><tr><td colspan="2"><strong>خصوصیات ظاهری </strong></td></tr></thead>']
    # # TBODIES = ['<tbody><tr><td>محل نصب</td><td>جلو</td></tr><tr><td>کد فنی</td><td>EZAROTE</td></tr><tr><td>سری ساخت</td><td>EZC100</td></tr><tr><td>نوع محصول</td><td>دسته گردان</td></tr><tr><td>کاربرد محصول</td><td>کنترل کلید از روی تابلو</td></tr><tr><td>تعداد قفل دسته گردان</td><td>حداکثر 3 تا</td></tr><tr><td>حالت نصب</td><td>با میله ی واسط</td></tr><tr><td>مدت زمان گارانتی</td><td>12 ماه</td></tr></tbody>', '<tbody><tr><td>رنگ بدنه</td><td>مشکی</td></tr></tbody>']
    # couunterhead = 1
    # for thead in THEADS:
    #     print(thead)
    #     print("thead" + str(couunterhead))
    #     couunterhead = couunterhead + 1

    # couunterbody = 1
    # for tbody in TBODIES:
    #     print(tbody)
    #     print("tbody" + str(couunterbody))
    #     couunterbody = couunterbody + 1






    # html_list = browser.find_element(By.CLASS_NAME, "list-unstyled")
    # items = html_list.find_elements(By.CSS_SELECTOR, "li")
    # for item in items:
    #     text = item.text

    # html_list = browser.find_element(By.CLASS_NAME, "extra_description")
    # items = html_list.find_elements(By.CSS_SELECTOR, "li")
    # for item in items:
    #     text = item.text

    table_parent = browser.find_element(By.CLASS_NAME, "table-responsive")
    table = table_parent.find_element(By.TAG_NAME, "table")
    table_html = table.get_attribute("outerHTML")
    print("Product information was taken.\n\n\n\n")
    print(table_html)
    

    browser.quit()

    return table_html






    # with open("PageNew.html", "w", encoding="utf8") as f:
    #     f.write(aaa)















# # acceptbtn = browser.find_element_by_class_selector("onetrust-accept-btn-handler")
# # acceptbtn.click()
# print(1)

# image = browser.find_element_by_class_selector(".zoom__img sc-pes-media-gallery-zoom")
# print(2)

# images_url = image.get_attribute("src")
# print(3)


# print(images_url)
# print(4)


# response = requests.get(images_url)
# print(5)


# open("my_Image.jpg", "wb").write(response.content)
# print(6)


# # with open('Logo.png', 'wb') as file:
    
# #     print(image)
# #     file.write(image.screenshot_as_png)


