from banner import banner_up
from getdata import start_scrapping_det
from H2X import html_add_2_excel
from X2H import read_excel
from writedata import go_to_safe_place 

banner_up()


whichone = str(input("if you need get data type (1) and if you need upload data type (2) : \n"))

if whichone == "1" :
    DetLink = input("Hello give me product Link : \n")
    excel_file_name = input("Choose an excel file name : \n")
    excel_file_name = excel_file_name
    
    html = start_scrapping_det(DetLink)
    print(html)
    html_add_2_excel(html, excel_file_name)   

    print("finish process please check " + excel_file_name + "file for your resault. :D ")

if whichone == "2" :
    excel_file_name = input("Choose an excel file name : \n")
    excel_file_name = excel_file_name
    print(read_excel)
        
    res = read_excel(excel_file_name)


    go_to_safe_place(excel_file_name, res)



# excel_file_path = input("Choose an excel file path : \n")


