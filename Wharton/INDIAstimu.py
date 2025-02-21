# importing required modules - (selenium , pandas , time)
 # selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 # Pandas imports
import pandas as pd
from pandas import DataFrame
 # Time
import time


# Data sets
   # list of id of tabs declared further in code
healthcare = {
    "Pharmaceuticals": [["524804","500087","500124","532482","500302","524715"],[]]
    }

technology = {
    "Computer services software and systems": [["532281","532129","500209","535648","532819","500304","532540","532755","507685"],[]] ,
    "Telecommunications equipment": [["532493"],[]] 
    }

consumerstaples = {
    "Foods": [["500790"],[]] ,
    "Personal care": [["532424","500696"],[]] ,
    "Agriculture fishing and ranching": [["540743"],[]] ,
    "Tobacco": [["500875"],[]]
    }

consumerdiscretionary = {
    "Auto parts": [["500530"],[]] ,
    "Restaurants": [["533155"],[]] ,
    "Automobiles": [["500520","532500","500570"],[]] ,
    "Recreational vehicles and boats": [["532977","500182"],[]] ,
    "Textiles apparel and shoes": [["500043"],[]] ,
    "Luxury items": [["500114"],[]] ,
    }

utilities = {
    "electrical":[["517300","532555","532898","500400"],[]] ,
    "telecom":[["532454","500108"],[]] , "gas":[["532155"],[]] 
    }

sectors = {
    "utilities": utilities , "healthcare": healthcare , "technology": technology ,
    "consumerstaples": consumerstaples , "consumerdiscretionary": consumerdiscretionary
    }

final_companies = []
final_beta = []
final_debt_equity = []
final_net_profit_margin = []
final_cash_profit = []
final_price_sales = []
final_price_earning = []
debt_equity_range = []
beta_range = []
net_profit_margin_range = []
god_number = 0

# Getting the input data
sector_input = input("Enter name of sector: ")
sector_input = sector_input.lower()
beta_input = input("Enter range for beta: ")
debt_equity_input = input("Enter range for Debt to Equity ratio: ")
net_profit_margin_input = input("Enter range of net profit margin: ")
a = sectors[sector_input]
print("Provide pe ratios range in order of the following: ")
print(list(a.keys()))
for i in sectors[sector_input]:
    price_earning_input = input("Enter range for pe: ")
    price_earning_input_low , price_earning_input_high = price_earning_input.split(":")
    price_earning_input_low , price_earning_input_high = float(price_earning_input_low) , float(price_earning_input_high)
    sectors[sector_input][i][1] = [price_earning_input_low , price_earning_input_high]

 # sorting ranges into predefined lists
beta_input_low , beta_input_high = beta_input.split(":")
beta_input_low , beta_input_high = float(beta_input_low) , float(beta_input_high)
beta_range = [beta_input_low , beta_input_high]

debt_equity_input_low , debt_equity_input_high = debt_equity_input.split(":")
debt_equity_input_low , debt_equity_input_high = float(debt_equity_input_low) , float(debt_equity_input_high)
debt_equity_range = [debt_equity_input_low , debt_equity_input_high]

net_profit_margin_input_low , net_profit_margin_input_high = net_profit_margin_input.split(":")
net_profit_margin_input_low , net_profit_margin_input_high = float(net_profit_margin_input_low) , float(net_profit_margin_input_high)
net_profit_margin_range = [net_profit_margin_input_low , net_profit_margin_input_high]


# setting up the chrome driver
path_of_webdriver = r"C:\Users\hride\OneDrive\Desktop\chromedriver.exe" 
driver = webdriver.Chrome(path_of_webdriver)
driver.maximize_window()

# setting up screener.in and moneycontrol
driver.get("https://www.screener.in/login/")
time.sleep(1)
 # interacting with login page
  # entering login details of screener.in
parent_list = driver.find_elements_by_class_name("form-field")
for index , parent in enumerate(parent_list):
    child_input = parent.find_element_by_tag_name("input")
    if index == 0:
        child_input.send_keys("Stockwarts.kwhs@gmail.com")
    else:
        child_input.send_keys("wharton14dede")
        child_input.send_keys(Keys.RETURN)

 # opening money control onto another tab
  # code to open a new fresh tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get("https://www.moneycontrol.com/")
# this sees if add has opened if so it closes it
try:
    f = driver.find_element_by_xpath("/html/body/div[@class='intes_container']/div[@class='headtop']/span[@class='textlik']/a")
    f.click()
except:
    pass

# coming back to screener.in
driver.switch_to.window(driver.window_handles[0])


# filtering companies
 # creating a flattened list to loop through 
list_unflat = []
list_flat = []
for i , j in list(sectors[sector_input].values()) :
    list_unflat.append(i)

def flat(a):
    for i in a:
        if type(i) == list:
            flat(i)
        else:
            list_flat.append(i)
flat(list_unflat)

for company_quote in list_flat:
    god_number += 1
     # getting price_earning range of industry
    for industry in sectors[sector_input]:
        if company_quote in sectors[sector_input][industry][0]:
            price_earning_range = [ sectors[sector_input][industry][1][0] , sectors[sector_input][industry][1][1] ]
            break
        else:
            pass


#                                              screener.in scraping  


    # scraping screener.in
     # searching company quote
    search_parent_screener = driver.find_element_by_class_name("search")
    search_screener_in = search_parent_screener.find_element_by_tag_name("input")
    search_screener_in.clear()
    search_screener_in.send_keys(company_quote)
    time.sleep(0.1)
    search_screener_in.send_keys(Keys.RETURN)
     # getting the ratio tags
    time.sleep(0.5)
    parent_ratios = driver.find_element_by_xpath("//div[@class = 'company-ratios']/ul[@id = 'top-ratios']")
    time.sleep(0.5)
    ratios_table = parent_ratios.find_elements_by_tag_name("li")
    ratio_list = []

     # ratio is the data storage for screener.in
    ratio = []
    
    for index in [3,10,11,12,13]:
        ratio_list.append(ratios_table[index])
     # getting ratio values
    for tag in ratio_list:
        var = tag.find_element_by_class_name("number")
        if var.text == "":
            ratio.append("N/A")
        else:
            ratio.append(var.text)
            
    price_earning , debt_equity , price_sales , net_profit , deprec = ratio
    # making sure deprec is positive
    if isinstance(deprec , str):
        pass
    else:
        if deprec < 0 :
            deprec = -1*deprec
        else:
            pass
        
    # making the data type of ratios string into float removing the comma  
    ratio = [price_earning , debt_equity , price_sales , net_profit , deprec]
    for index , str_ratio in enumerate(ratio):
        if str_ratio == "N/A":
            continue
        temp_list = str_ratio.split(",")
        var = ""
        for char in temp_list:
            var += char
        ratio[index] = float(var)
        
    # adding cash profit and removing net profit and depreciation
    cash_profit = ratio[3] + ratio[4]
    if isinstance(cash_profit , str):
        cash_profit == "N/A"
    ratio.pop()
    ratio[3] = cash_profit


#                                              Money control scraping  


     # data storage for money control
      # data_moey_ctrl has beta as first value and net profit margin as second
    ratio_money_ctrl = ["Beta_value" , "Net_profit_margin"]
    
    # scraping data from moneycontrol
     # switching tab to money control
    driver.switch_to.window(driver.window_handles[1])

    # locating the input box and entering company name letter by letter becuz site doesnt show suggested list if company name pasted     
    element_search = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.ID, "search_str")))
    for letter in list(company_quote):
        element_search.send_keys(letter)
        time.sleep(0.5)

    # finding <a> tag of the company from the suggested list and clicking it. 
     # when the first time moneycontrol opens path is different
    if god_number == 1:
        char = "/html/body/div[@id='mc_mainWrapper']/header[@class=' responsive_true ']/div[@class='header_desktop header1024']/div[@class='topnav']/div[@class='main_header_wrapper']/div[@class='clearfix']/div[@class='top_search_wrap']/div[@class='searchBox searchfloat clearfix FL']/div[@class='searchboxInner clearfix PR FL']/form[@id='form_topsearch']/div[@id='autosugg_mc1']/div[@id='autosuggestlist']/ul[@class='suglist scrollBar']/li[1]/a"
    else:
        char = "/html/body[@class='container1280']/header[@class=' responsive_true ']/div[@class='header_desktop ']/div[@class='topnav']/div[@class='main_header_wrapper']/div[@class='clearfix']/div[@class='top_search_wrap']/div[@class='searchBox searchfloat clearfix FL']/div[@class='searchboxInner clearfix PR FL']/form[@id='form_topsearch']/div[@id='autosugg_mc1']/div[@id='autosuggestlist']/ul[@class='suglist scrollBar']/li[1]/a"
    search = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH, char )))
    search.click()

    # find the beta value
    char = "/html/body[@class='container1280']/section[@id='mc_content']/div[@class='price_chartpg']/section[@id='sec_quotes']/div[@class='main_wrapper_res corporate-wrapper']/div[@class='moneyprice_bx']/div[@class='nsbs_maincnt nsbs_block']/div[@id='div_bse_nse_livebox_wrap']/div[@id='div_bse_livebox_wrap']/div[@class='bsedata_bx']/div[@class='clearfix mkt_openclosebx']/div[@class='open_lhs2']/div[@class='lowhigh_wrap']/ul[@class='clearfix vwaplist']/li[1]/div[@class='disin vt'][2]/span[2]"
    beta = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH, char )))
    beta_value = beta.text
    ratio_money_ctrl[0] = float(beta_value)

    # navigating to net profit margin
     # navigating to finance button from top bar
#   char = "/html/body[@class='container1280']/section[@id='mc_content']/div[@class='price_chartpg']/section[@id='sec_quotes']/div[@class='main_wrapper_res corporate-wrapper']/div[@class='moneyprice_bx']/div[@class='clearfix MT10']/div[@class='nav2 PR clearfix']/div[@class='hidenav_mobile']/div[@class='fixednav']/nav[@class='mainstknav']/div[@class='forbgmax clearfix']/ul/li[@class=' main_sticky_menu '][7]/a"
 #char = "/html/body[@class='container1280']/section[@id='mc_content']/div[@class='price_chartpg']/section[@id='sec_quotes']/div[@class='main_wrapper_res corporate-wrapper']/div[@class='moneyprice_bx']/div[@class='clearfix MT10']/div[@class='nav2 PR clearfix']/div[@class='hidenav_mobile']/div[@class='fixednav menu_sec_desk']/nav[@class='mainstknav']/div[@class='forbgmax clearfix']/ul/li[@class=' main_sticky_menu '][7]/a"
    #finance = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH, char)))
    #finance.click()

    time.sleep(4)
    # navigating to ratios button from top bar which takes to new tab
#    char = "/html/body[@class='container1280']/section[@id='mc_content']/div[@class='price_chartpg']/section[@id='sec_quotes']/div[@class='main_wrapper_res corporate-wrapper']/div[@class='moneyprice_bx']/div[@class='clearfix MT10']/div[@class='nav2 PR clearfix']/div[@class='hidenav_mobile']/div[@class='fixednav menu_sec_desk']/nav[@class='mainstknav']/div[@class='forbgmax clearfix']/ul/li[@class=' main_sticky_menu '][7]/ul/li[8]/a"
    char = "/html/body[@class='container1280']/section[@id='mc_content']/div[@class='price_chartpg']/section[@id='sec_quotes']/div[@class='main_wrapper_res corporate-wrapper']/div[@class='moneyprice_bx']/div[@class='clearfix MT10']/div[@class='nav2 PR clearfix']/div[@class='hidenav_mobile']/div[@class='fixednav menu_sec_desk']/nav[@class='mainstknav']/div[@class='forbgmax clearfix']/ul/li[@class=' main_sticky_menu '][7]/ul/li[8]/a"
    ratios = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH, char)))
    ratios.click()

    #switching to new tab
    driver.switch_to.window(driver.window_handles[2])

    #switching to tab with consolidated data by changing the url
    url = driver.current_url
    print(url)
    split = url.split("/")
    split[5] = "consolidated-ratiosVI"
     # adding the '/' back to each item
    for index , j in enumerate(split):
        j+= '/'
        split[index] = j
     # creating the new url   
    new_url = ''
    for i in split:
        new_url += i
    driver.get(new_url)

    # getting net_profit_margin
    char = "/html/body[@class='container1280']/section[@id='mc_content']/div[@class='price_chartpg']/div[@class='main_wrapper_res clearfix']/div[@class='financial-section']/div[@class='tab-content clearfix']/div[@id='new-format']/div[@class='tab-content']/div[@id='standalone-new']/div[@class='table-responsive financial-table']/table[@class='mctable1']/tbody/tr[18]/td[2]"
    try:
        npm = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH, char)))
        net_profit_margin = npm.text
        ratio_money_ctrl[1] = float(net_profit_margin)

    except :
        ratio_money_ctrl[1] =  "N/A"




    # closing and going back to screener
    driver.close()
    driver.switch_to.window(driver.window_handles[0])




    # dictionar to loop to filter
    data_dict = {
            "price_earning": [ratio[0] , price_earning_range[0] , price_earning_range[1]] ,
            "debt_equity": [ratio[1] , debt_equity_range[0] , debt_equity_range[1]] ,
            "net_profit_margin": [ratio_money_ctrl[1] , net_profit_margin_range[0] , net_profit_margin_range[1]] ,
            "beta": [ratio_money_ctrl[0] , beta_range[0] , beta_range[1]] ,
            "cash_profit" : [ratio[3]] ,
            "price_sales" : [ratio[2]]
                            }


    # filtering the company
    error = 0
    for ratio_name in data_dict:
        if ratio_name in ["cash_profit" , "price_sales"]:
            continue
        if isinstance(data_dict[ratio_name][0] , float):
#                      ratio data                range low                   ratio data                 range high
            if data_dict[ratio_name][0] < data_dict[ratio_name][1] or data_dict[ratio_name][0] > data_dict[ratio_name][2]:
                error += 1
            else:
                pass
        else:
            pass
    # checking if company passed criteria
    if error > 2 :
        pass
     # company passing criteria and data getting saved
    else:
        final_companies.append(company_quote)
        final_beta.append(data_dict["beta"][0])
        final_debt_equity.append(data_dict["debt_equity"][0])
        final_net_profit_margin.append(data_dict["net_profit_margin"][0])
        final_cash_profit.append(data_dict["cash_profit"][0])
        final_price_sales.append(data_dict["price_sales"][0])
        final_price_earning.append(data_dict["price_earning"][0])     


# Organising the data in cash profit and sales profit criteria
list_of_data = list(zip(final_companies , final_cash_profit , final_price_sales , final_beta , final_debt_equity , final_price_earning , final_net_profit_margin))

  # Converting the tupple into lists to replace N/A values to an int
for index , tuple_ in enumerate(list_of_data):
    list_of_data[index] = list(tuple_)

for data in list_of_data:
    if isinstance(data[1] , str):
        data[1] = -999999999999999999999999999999999999999999999999999999999999999999999999999999

    if isinstance(data[2] , str):
        data[2] = 999999999999999999999999999999999999999999999999999999999999999999999999999999

 # Organising lists and converting them to dataframe
org_cash_profit = sorted(list_of_data , key = lambda x: x[1])
org_price_sales = sorted(list_of_data , key = lambda x: x[2] , reverse = True)

list_cash_profit = list(zip(*org_cash_profit))
list_price_sales = list(zip(*org_price_sales))


# replacing 99999.... values with N/A
 # making the tuples to list 
for index , tuple_a in enumerate(list_cash_profit):
    list_cash_profit[index] = list(tuple_a)

for index , tuple_b in enumerate(list_price_sales):
    list_price_sales[index] = list(tuple_b)
    
 # replacing 99....
for index , item_a in enumerate(list_cash_profit[1]):
    if item_a == -999999999999999999999999999999999999999999999999999999999999999999999999999999:
        list_cash_profit[1][index] = "N/A"

for index , item_b in enumerate(list_cash_profit[2]):
    if item_b == 999999999999999999999999999999999999999999999999999999999999999999999999999999:
        list_cash_profit[2][index] = "N/A"

for index , item_c in enumerate(list_price_sales[1]):
    if item_c == -999999999999999999999999999999999999999999999999999999999999999999999999999999:
        list_price_sales[1][index] = "N/A"

for index , item_d in enumerate(list_price_sales[2]):
    if item_d == 999999999999999999999999999999999999999999999999999999999999999999999999999999:
        list_price_sales[2][index] = "N/A"

  # data frames                                                       
df_cash_profit = DataFrame({"Company": list_cash_profit[0] ,"Cash_Profit": list_cash_profit[1] , "Price_Sales": list_cash_profit[2] , "Beta": list_cash_profit[3] , "Debt_Equity": list_cash_profit[4] , "Price_Earning": list_cash_profit[5] , "Net_Profit_Margin": list_cash_profit[6]})
df_price_sales = DataFrame({"Company": list_price_sales[0] ,"Price_Sales": list_price_sales[2] , "Cash_Profit": list_price_sales[1] , "Beta": list_price_sales[3] , "Debt_Equity": list_price_sales[4] , "Price_Earning": list_price_sales[5] , "Net_Profit_Margin": list_price_sales[6]})
pd.set_option("display.max_columns", None)

# printing screener results
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Cash_Profit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
print(df_cash_profit)
print("\n \n")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Price_Sales ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df_price_sales)
