import pandas as pd
from pandas import DataFrame
import requests
import json
import time

# pre defined variables
healthcare = {
    "Pharmaceuticals": [["ABBV","BMY","ENDP","GILD","GSK","GMED","GMED","JNJ","MRK","NVS","PFE","PBH","TEVA","ZGNX"],[]] ,
    "Health care services": [["ACHC"],[]] ,
    "Biotechnology": [["AMGN","CGIX","CPRX","MYGN","REGN"],[]] ,
    "Health care services": [["AMN","TVTY"],[]] ,
    "Medical equipment": [["BAX","ILMN"],[]] ,
    "Medical & dental instruments & supplies": [["CSII"],[]] ,
    "Health care management services": [["CNC","UNH"],[]]
    }

technology = {
    "Computer services software and systems": [["ADBE","BABA","GOOG","ANET","BIDU","BNFT","CTSH","DXC","FB","GRPN","MANH","MSFT","NTES","ORCL","SINA","WORK","SOHU","TWTR"],[]] ,
    "Computer technology": [["AAPL"],[]] ,
    "Semiconductors and components": [["NXPI"],[]] ,
    "Electronic entertainment": [["NCTY","ZNGA"],[]] ,
    "Telecommunications equipment": [["UTSI"],[]]
    }

consumerstaples = {
    "Foods": [["CPB","GIS","JJSF","K","MKC","SYY","HSY","THS","TSN","UNFI"],[]] ,
    "Drug and grocery store chains": [["CASY",],[]] ,
    "Soft drinks": [["KO","KDP","MNST","FIZZ","PEP",],[]] ,
    "Personal care": [["CL","PG","WDFC"],[]] ,
    "Drug and grocery store chains": [["CVS","MCK","RAD","SFM"],[]] ,
    "Brewers and distillers": [["TAP"],[]]
    }
#"Foods": [["CPB","CTVA","GIS","JJSF","K","MKC","SYY","HSY","TR","THS","TSN","UNFI"],[]] ,

#"Personal care": [["CL","PG","UL","WDFC"],[]] ,
consumerdiscretionary = {
    "Specialty retail": [["ANF","AEO","BNED","BBBY","BBY","BBW","BURL","KMX","FL","GPS","HIBB","TLRD","TCS","TJX","ULTA","URBN"],[]] ,
    "Advertising agencies": [["ATV"],[]] ,
    "Diversified retail": [["AMZN","CORE","COST","DG","DLTR","DOL","LE","M","SFIX","TGT"],[]] ,
    "Auto parts": [["APTV","BWA","CAAS"],[]] ,
    "Cosmetics": [["AVP","REV"],[]] ,
    "Restaurants": [["CAKE","CMG","DPZ","MCD","PZZA","SBUX","TXRH","WEN","YUM"],[]] ,
    "Cable television services": [["CMCSA"],[]] ,
    "Publishing": [["DJCO"],[]] ,
    "Automobiles": [["V","GM","HMC","TSLA","TM"],[]] ,
    "Consumer services Miscellaneous": [["HRB","LYFT","RBA","UBER"],[]] ,
    "Recreational vehicles and boats": [["HOG","LCII"],[]] ,
    "Toys" : [["HAS","MAT"],[]] ,
    "Hotel/motel": [["H","MAR","RLH","WYND"],[]] ,
    "Entertainment": [["IMAX","DIS"],[]] ,
    "Casinos and gambling": [["LVS"],[]] ,
    "Textiles apparel and shoes": [["LULU","NKE","UAA","VRA","VFC"],[]] ,
    "Luxury items": [["MOV","TIF"],[]] ,
    "Education services": [["EDU","TAL"],[]] ,
    "Leisure time": [["NCLH","PLNT","SWBI"],[]] ,
    "Radio and TV broadcasters": [["SIRI"],[]]
    }

utilities = {
    "electrical":[["AEP","D","FE","HNP","PCG","SO"],[]] , "water":[["AWK","MSEX","SJW","YORW"],[]] ,
    "telecom":[["T","CHL","CHA","CHU","GOGO","GTT","VZ","VOD"],[]] , "gas":[["NFG","UGI"],[]] , "others":[["SRE"],[]]
    }

sectors = {
    "utilities": utilities , "healthcare": healthcare , "technology": technology ,
    "consumerstaples": consumerstaples , "consumerdiscretionary": consumerdiscretionary
    }

final_companies = []
list_of_companies = []
final_beta = []
final_debt_equity = []
final_net_profit_margin = []
final_cash_profit = []
final_price_sales = []
final_price_earning = []
final_price_sales_copy = []
final_cash_profit_copy = []
num_cash_profit = 0
num_price_sales = 0

# basic inputs
print('\n\n')
print("                             Supreme Deluxe Prime                     ")
print("                        USA Economy Stock Screener      \n          ")
print("                               Limited Edition                        ")
print("\n") 
while True:
    sector_input = input("Enter name of sector: ")
    sector_input = sector_input.lower()
    if sector_input in ["hridey","atharv"]:
        time.sleep(1)
        print("\n")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Pls   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Welcome   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   The Famous   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~   The Legendary   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~    The One and Only   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print("\n")
        print("                               ``` {} ```".format(sector_input))
        print("\n")
        print("\n")
        time.sleep(2)

    else:
        break
beta_input = input("Enter range for beta: ")
debt_equity_input = input("Enter range for Debt to Equity ratio: ")
net_profit_margin_input = input("Enter range of net profit margin: ")
a = sectors[sector_input]
print("\nProvide pe ratios range in order of the following: \n")
print(list(a.keys()))
for i in sectors[sector_input]:
    price_earning_input = input("Enter range for pe: ")
    price_earning_input_low , price_earning_input_high = price_earning_input.split(":")
    price_earning_input_low , price_earning_input_high = float(-99999999999999999999999999999999999999999999999999999999999999999) , float(price_earning_input_high)
    sectors[sector_input][i][1] = [price_earning_input_low , price_earning_input_high]
# key value
key = "86cf3ecd5500ca81857b8321a24fdeb8"

beta_input_low , beta_input_high = beta_input.split(":")
beta_input_low , beta_input_high = float(-99999999999999999999999999999999999999999999999999999999999999999) , float(beta_input_high)

debt_equity_input_low , debt_equity_input_high = debt_equity_input.split(":")
debt_equity_input_low , debt_equity_input_high = float(-99999999999999999999999999999999999999999999999999999999999999999) , float(debt_equity_input_high)

net_profit_margin_input_low , net_profit_margin_input_high = net_profit_margin_input.split(":")
net_profit_margin_input_low , net_profit_margin_input_high = float(net_profit_margin_input_low) , float(99999999999999999999999999999999999999999999999999999999999999999)

# function that gets the data of a company
def get_company_data(quote,key):
    # requesting the data
    ratios = requests.get("https://financialmodelingprep.com/api/v3/ratios/{}?limit=40&apikey={}".format(quote,key))
    beta_data = requests.get("https://financialmodelingprep.com/api/v3/profile/{}?apikey={}".format(quote,key))
    #cash_flow = requests.get("https://financialmodelingprep.com/api/v3/cash-flow-statement/{}?limit=120&apikey={}".format(quote,key))
    
    # converting the data into python dictionaries wiht latest data
    ratios = ratios.text
    beta_data = beta_data.text
    #cash_flow = cash_flow.text
    try:
        ratios = json.loads(ratios)[0]
    except:
        ratios = {"priceEarningsRatio": "N/A" , "debtEquityRatio" : "N/A" , "netProfitMargin" : "N/A"}
    try:
        beta_data = json.loads(beta_data)[0]
    except:
        beta_data = {"beta" : "N/A"}

    # getting the required data
    price_earning = ratios["priceEarningsRatio"]
    debt_equity = ratios["debtEquityRatio"]
    net_profit_margin = ratios["netProfitMargin"]
    beta = beta_data["beta"]

    # printing company data that is not found
    temp_dict = {
        "price_earning": price_earning , "debt_equity": debt_equity ,
        "net_profit_margin": net_profit_margin , "beta": beta
        }
    for i in temp_dict:
        if isinstance(temp_dict[i],float) or isinstance(temp_dict[i],int):
            pass
        else:
            pass
#            print("{} - {} - {} unknown".format(quote,i,temp_dict[i]))
    
    # returning the data
    return [price_earning , debt_equity ,  net_profit_margin , beta]

def company_screening():
    global sector_input , sectors , healthcare , technology , utilities , consumerstaples , consumerdiscretionary
    global beta_input_low , beta_input_high
    global debt_equity_input_low , debt_equity_input_high
    global net_profit_margin_input_low , net_profit_margin_input_high  
    global list_of_companies , final_companies

    #key value
    global key
    
    # getting a list of companies to filter
    a = sectors[sector_input]
    b = list(a.values())
    c = []
    for i in b:
        c.append(i[0]) 
    def flatlist(l):
        global list_of_companies
        for x in l:
            if type(x) == list:
                flatlist(x)
            else:
                list_of_companies.append(x)
    flatlist(c)
    
    # filtering the list
    for company in list_of_companies:
        count = 0
        price_earning , debt_equity , net_profit_margin , beta  = get_company_data(company,key)
        for i in sectors[sector_input]:
            if company in sectors[sector_input][i][0]:
                price_earning_industry_low = sectors[sector_input][i][1][0]
                price_earning_industry_high = sectors[sector_input][i][1][1]
                break
            else:
                pass
        data_dict = {
            "price_earning": [price_earning , price_earning_industry_low , price_earning_industry_high] ,
            "debt_equity": [debt_equity , debt_equity_input_low , debt_equity_input_high] ,
            "net_profit_margin": [net_profit_margin , net_profit_margin_input_low , net_profit_margin_input_high] ,
            "beta": [beta , beta_input_low , beta_input_high] 
                            }

        for i in data_dict:
            if isinstance(data_dict[i][0] , float) or isinstance(data_dict[i][0] , int):
                if data_dict[i][0] <= data_dict[i][1] or data_dict[i][0] >= data_dict[i][2]:
                    count += 1
                else:
                    pass
            else:
                pass

        if count > 2:
            pass
        else:
            final_companies.append(company)

# code output
company_screening()

#list of final betas

for company in final_companies:
    cash_flow = requests.get("https://financialmodelingprep.com/api/v3/cash-flow-statement/{}?limit=120&apikey={}".format(company,key))
    cash_flow = cash_flow.text
    try:
        cash_flow = json.loads(cash_flow)[0]
        net_income = cash_flow["netIncome"]
        depreciation_amortization = cash_flow["depreciationAndAmortization"]
        cash_profit = net_income + depreciation_amortization
        if isinstance(cash_profit , float) or isinstance(cash_profit , int):
            pass
        else:
            cash_profit = "N/A"
    except:
        cash_profit = "N/A"
    final_cash_profit.append(cash_profit)        
    
for company in final_companies:
    beta_data = requests.get("https://financialmodelingprep.com/api/v3/profile/{}?apikey={}".format(company,key))
    beta_data = beta_data.text
    try:
        beta_data = json.loads(beta_data)[0]
        beta = beta_data["beta"]
    except:
        beta = "N/A"
    final_beta.append(beta)

# list of final ratios
for company in final_companies:
    ratio_data = requests.get("https://financialmodelingprep.com/api/v3/ratios/{}?limit=40&apikey={}".format(company,key))
    ratios = ratio_data.text
    try:
        ratios = json.loads(ratios)[0]
        price_earning = ratios["priceEarningsRatio"]
        debt_equity = ratios["debtEquityRatio"]
        net_profit_margin = ratios["netProfitMargin"]
        price_sales = ratios["priceToSalesRatio"]
    except:
        price_earning = "N/A"
        debt_equity = "N/A"
        net_profit_margin = "N/A"
        price_sales = "N/A"
        
    final_debt_equity.append(debt_equity)
    final_price_earning.append(price_earning)
    final_net_profit_margin.append(net_profit_margin)
    final_price_sales.append(price_sales)

list_of_data = list(zip(final_companies , final_cash_profit , final_price_sales , final_beta , final_debt_equity , final_price_earning , final_net_profit_margin))
for i , j in enumerate(list_of_data):
    var = list(j)
    list_of_data[i] = var

for i , j in enumerate(list_of_data):
    if isinstance(list_of_data[i][1] , int) or isinstance(list_of_data[i][1] , float):
        pass
    else:
        list_of_data[i][1] = -99999999999999999999999999999999999999999999999999999999999999999

    if isinstance(list_of_data[i][2] , int) or isinstance(list_of_data[i][2] , float):
        pass
    else:
        list_of_data[i][2] = 9999999999999999999999999999999999999999999999999999999999999999999

org_cash_profit = sorted(list_of_data , key = lambda x: x[1])
org_price_sales = sorted(list_of_data , key = lambda x: x[2] , reverse = False)

list_cash_profit = list(zip(*org_cash_profit))
list_price_sales = list(zip(*org_price_sales))

for x in [list_cash_profit , list_price_sales]:
    for i , j in enumerate(x):
        if j== 9999999999999999999999999999999999999999999999999999999999999999999 or j == -99999999999999999999999999999999999999999999999999999999999999999:
            x[i] = "N/A"
df_cash_profit = DataFrame({"Company": list_cash_profit[0] ,"Cash_Profit": list_cash_profit[1] , "Price_Sales": list_cash_profit[2] , "Beta": list_cash_profit[3] , "Debt_Equity": list_cash_profit[4] , "Price_Earning": list_cash_profit[5] , "Net_Profit_Margin": list_cash_profit[6]})
df_price_sales = DataFrame({"Company": list_price_sales[0] ,"Cash_Profit": list_price_sales[1] , "Price_Sales": list_price_sales[2] , "Beta": list_price_sales[3] , "Debt_Equity": list_price_sales[4] , "Price_Earning": list_price_sales[5] , "Net_Profit_Margin": list_price_sales[6]})

pd.set_option("display.max_columns", None)
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Cash_Profit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
print(df_cash_profit)
print("\n \n")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Price_Sales ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df_price_sales)