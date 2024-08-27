import gspread
import datetime
import time



gc = gspread.service_account(filename='albiononlinemarketcheckingbot-e064af3d1551.json')
sh = gc.open("Albion Online Market Data Bot")

def uploadData(priceList, tier, enchantement, city, payment):
    
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d-%m %H:%M')
    timeList = []
    for i in range(5):
        timeList.append(timestamp)

    # Choosing sheet for data upload
    cityData = {'1': "Thetford",
                '2': "FortSterling",
                '3': "Lymhurst",
                '4': "Bridgewatch",
                '5': "Martlock"}
    
    if city in cityData:
        sheet = cityData.get(city)
    if enchantement == '0':
        worksheet = sh.worksheet(sheet)   
    if enchantement == '1':
        worksheet = sh.worksheet(sheet+enchantement)
    if enchantement == '2':
        worksheet = sh.worksheet(sheet+enchantement)

    # Choosing cells for data upload
    
    tierData = []

    if payment == '1':
        tierData = {'4': "B",
                '5': "C",
                '6': "D", 
                '7': "E",
                '8': "F"}
       
    if payment == '2':
        tierData = {'4': "H",
                '5': "I",
                '6': "J", 
                '7': "K",
                '8': "L"}

    if tier in tierData:
        cellLetter = tierData.get(tier)
        cellAddress = cellLetter + str(1)
    print('worksheet: ', worksheet)
    print('cellAdress: ', cellAddress)    
    worksheet.update(cellAddress, [[e] for e in priceList], value_input_option="USER_ENTERED")
    worksheet.update(cellLetter+'82', [[e] for e in timeList], value_input_option="USER_ENTERED")
    return

def uploadBmData(priceList, countList, tier, enchantement, part):

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d-%m %H:%M')
    timeList = []
    for i in range(5):
        timeList.append(timestamp)

    # Choosing sheet for data upload
    sheet = 'BlackMarket'
    if enchantement == '0':
        worksheet = sh.worksheet(sheet)   
    if enchantement == '1':
        worksheet = sh.worksheet(sheet+enchantement)
    if enchantement == '2':
        worksheet = sh.worksheet(sheet+enchantement)

    # Choosing cells for data upload
    tierData = {'4': "B",
                '5': "D",
                '6': "F", 
                '7': "H",
                '8': "J"}

    countData = {'4': "C",
                '5': "E",
                '6': "G", 
                '7': "I",
                '8': "K"}
    
    tierPart = {'1': "1",
                '2': "27",
                '3': "52", 
                '4': "66",
                '5': "77"}

    if tier in tierData:
        cellLetterPrice = tierData.get(tier)
    
    if tier in countData:
        cellLetterCount = countData.get(tier)

    if part in tierPart:
        cellNumber = tierPart.get(part)

    cellAddressPrice = cellLetterPrice+cellNumber
    cellAddressCount = cellLetterCount+cellNumber
    print('cellAdressPrice: ', cellAddressPrice)
    print('cellAdressCount: ', cellAddressCount)     
    worksheet.update(cellAddressPrice, [[e] for e in priceList], value_input_option="USER_ENTERED")
    worksheet.update(cellAddressCount, [[e] for e in countList], value_input_option="USER_ENTERED")
    worksheet.update(cellLetterPrice+'82', [[e] for e in timeList], value_input_option="USER_ENTERED")
    return

def downloadData(tier, enchantment, payment):

    worksheet = sh.worksheet('Main')

    list_of_lists = worksheet.get_all_values()
    
    return list_of_lists

def uploadCreatedBuyOrdersToSheets(itemNames, itemInfos, amounts, boughtAmounts, orderTotals, budgets, cities, itemExpensive, enteredProfit, itemProfit):
    
    worksheet = sh.worksheet('Bought')
    worksheet.batch_clear(["A2:K50"])
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d-%m %H:%M')
    timeList = []
    for i in range(len(itemNames)):
        timeList.append(timestamp)

    worksheet.update('A2', [[e] for e in itemNames], value_input_option="USER_ENTERED")
    worksheet.update('B2', [[e] for e in itemInfos], value_input_option="USER_ENTERED")
    worksheet.update('C2', [[e] for e in amounts], value_input_option="USER_ENTERED")
    worksheet.update('D2', [[e] for e in boughtAmounts], value_input_option="USER_ENTERED")
    worksheet.update('E2', [[e] for e in orderTotals], value_input_option="USER_ENTERED")
    worksheet.update('F2', [[e] for e in budgets], value_input_option="USER_ENTERED")
    worksheet.update('G2', [[e] for e in cities], value_input_option="USER_ENTERED")
    worksheet.update('H2', [[e] for e in timeList], value_input_option="USER_ENTERED")
    worksheet.update('I2', [[e] for e in itemExpensive], value_input_option="USER_ENTERED")
    worksheet.update('J2', [[e] for e in enteredProfit], value_input_option="USER_ENTERED")
    worksheet.update('K2', [[e] for e in itemProfit], value_input_option="USER_ENTERED")

    for i in range(len(itemNames)):
        print(itemNames[i], " ", itemInfos[i], " ", amounts[i], " ", boughtAmounts[i], " ", orderTotals[i], " ", budgets[i], " ", cities[i], " ", timeList[i], " ", itemExpensive[i],
              " ", enteredProfit[i], " ", itemProfit[i])
    return
