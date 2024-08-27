import pyautogui
import keyboard
import time
from getRandomCoordinates import *
from getRandomDuration import *
from listOfAll_Items import *
from ItemOperations import *
from coordinates import *
from dataToGoogleSheet import *
from getProfitedItems import *

def orderBuy(tier, enchantment, city, profit, budget):

    paymentCords = buyOrderFirst
    tierList = []
    enchList = []
    convertedBudget = int(budget)
    money = int(budget)
    if len(tier) > 1:
        tierList.extend(tier)
    else:
        tierList.extend(tier)
    if len(enchantment) > 1:
        enchList.extend(enchantment)
    else:
        enchList.extend(enchantment)

    unusualitemDict = {
        "Adept's Halberd": meleeCords,
        "Adept's Claws": meleeCords, 
        "Adept's Hammer": meleeCords,
        "Adept's Mace": meleeCords,
        "Adept's Crossbow": rangedCords,
        "Adept's Shield": offHandCords
    }

    
    itemName = []
    itemInfo = []
    leftBudget = []
    boughtAmount = []
    itemCity = []
    itemOrdersTotalCost = []
    totalAmount = []
    itemExpensive = []
    enteredProfit = []
    itemProfit = []
    budget_exhausted = False
    for e in enchList:

        # Getting enchantments buttons coordinates by enchantment options
        dataEnchantements = {'0': ench0Overal,
                            '1': ench1Overal,
                            '2': ench2Overal}
        
        if e in dataEnchantements:
            enchantementCord = dataEnchantements.get(e)

        pyautogui.moveTo(getRandomCoordinates(defaultOverallEnch), duration=getRandomDuration())
        pyautogui.leftClick()
        pyautogui.moveTo(getRandomCoordinates(enchantementCord), duration=getRandomDuration())
        pyautogui.leftClick()

        for t in tierList:
            
            sheetList = downloadData(t, e, 'o')
            itemsList = getProfitedItems(sheetList, city, profit)

            dataTiers = {'4': tier4Overal,
                        '5': tier5Overal,
                        '6': tier6Overal,
                        '7': tier7Overal,
                        '8': tier8Overal}
        
            if t in dataTiers:
                tierCord = dataTiers.get(t)

            pyautogui.moveTo(getRandomCoordinates(defaultOveralTier), duration=getRandomDuration())
            pyautogui.leftClick()
            pyautogui.moveTo(getRandomCoordinates(tierCord), duration=getRandomDuration())
            pyautogui.leftClick()

            for item in itemsList:
                name = item[0]
                c = item[5]
                price = int(item[3])
                info = t+e+'o'
                if budget_exhausted is False:
                    unusualCord = unusualitemDict.get(item[0])
                    pyautogui.moveTo(getRandomCoordinates(categoryDefaultCords), duration=getRandomDuration())
                    pyautogui.leftClick()

                    if not unusualCord:
                        pyautogui.moveTo(getRandomCoordinates(allCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                    else:
                        pyautogui.moveTo(getRandomCoordinates(unusualCord), duration=getRandomDuration())
                        pyautogui.leftClick()

                    pyautogui.moveTo(getRandomCoordinates(revertBTN_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
                    pyautogui.moveTo(getRandomCoordinates(searchBar_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
                    keyboard.write(item[0])
                    time.sleep(0.3)
                    pyautogui.moveTo(getRandomCoordinates(createBuyOrderBTN_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
      
                    amount = generateAmount(item[2], money, t)
                    total_purchased, total_spent, price_flag, budget_exhausted = orderBuyOperations(paymentCords, amount, price, money, name)

                    money -= total_spent
                    if price_flag == 'Good':
                        itemName.append(name)
                        itemInfo.append(info)

                        totalAmount.append(amount)
                        boughtAmount.append(total_purchased)
                        itemOrdersTotalCost.append(total_spent)
                        leftBudget.append(money)
                        itemCity.append(c)
                        enteredProfit.append(profit)
                        itemProfit.append(item[4])
                        itemExpensive.append(price_flag)

                else:
                    print('0 money left')
                    break
                print('All items bought')
    #upload data to google after all orders
    uploadCreatedBuyOrdersToSheets(itemName, itemInfo, totalAmount, boughtAmount, itemOrdersTotalCost, leftBudget, itemCity, itemExpensive, enteredProfit, itemProfit)
    return


def fastBuy(tier, enchantment, city, profit, budget):

    tierList = []
    enchList = []
    convertedBudget = int(budget)
    money = int(budget)
    if len(tier) > 1:
        tierList.extend(tier)
    else:
        tierList.extend(tier)
    if len(enchantment) > 1:
        enchList.extend(enchantment)
    else:
        enchList.extend(enchantment)

    unusualitemDict = {
        "Adept's Halberd": meleeCords,
        "Adept's Claws": meleeCords, 
        "Adept's Hammer": meleeCords,
        "Adept's Mace": meleeCords,
        "Adept's Crossbow": rangedCords,
        "Adept's Shield": offHandCords
    }
 
    itemName = []
    itemInfo = []
    leftBudget = []
    boughtAmount = []
    itemCity = []
    itemOrdersTotalCost = []
    totalAmount = []
    itemExpensive = []
    enteredProfit = []
    itemProfit = []
    budget_exhausted = False
    for e in enchList:
        # Getting enchantments buttons coordinates by enchantment options
        dataEnchantements = {'0': ench0Overal,
                            '1': ench1Overal,
                            '2': ench2Overal}
        
        if e in dataEnchantements:
            enchantementCord = dataEnchantements.get(e)

        pyautogui.moveTo(getRandomCoordinates(defaultOverallEnch), duration=getRandomDuration())
        pyautogui.leftClick()
        pyautogui.moveTo(getRandomCoordinates(enchantementCord), duration=getRandomDuration())
        pyautogui.leftClick()

        for t in tierList:
            
            sheetList = downloadData(t, e, 'f')
            itemsList = getProfitedItems(sheetList, city, profit)

            dataTiers = {'4': tier4Overal,
                        '5': tier5Overal,
                        '6': tier6Overal,
                        '7': tier7Overal,
                        '8': tier8Overal}
        
            if t in dataTiers:
                tierCord = dataTiers.get(t)

            pyautogui.moveTo(getRandomCoordinates(defaultOveralTier), duration=getRandomDuration())
            pyautogui.leftClick()
            pyautogui.moveTo(getRandomCoordinates(tierCord), duration=getRandomDuration())
            pyautogui.leftClick()

            for item in itemsList:
                name = item[0]
                c = item[5]
                price = int(item[3])
                info = t+e+'f'
                if budget_exhausted is False:
                    unusualCord = unusualitemDict.get(name)
                    print('budget left: ', money)
                    pyautogui.moveTo(getRandomCoordinates(categoryDefaultCords), duration=getRandomDuration())
                    pyautogui.leftClick()

                    if not unusualCord:
                        pyautogui.moveTo(getRandomCoordinates(allCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                    else:
                        pyautogui.moveTo(getRandomCoordinates(unusualCord), duration=getRandomDuration())
                        pyautogui.leftClick()

                    pyautogui.moveTo(getRandomCoordinates(revertBTN_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
                    pyautogui.moveTo(getRandomCoordinates(searchBar_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
                    keyboard.write(name)
                    time.sleep(0.5)
                    amount = generateAmount(item[2], money, t)
                    total_purchased, total_spent, price_flag, budget_exhausted = fastBuyOperations(amount, price, money, name)

                    money -= total_spent
                    if price_flag == 'Good':
                        itemName.append(name)
                        itemInfo.append(info)

                        totalAmount.append(amount)
                        boughtAmount.append(total_purchased)
                        itemOrdersTotalCost.append(total_spent)
                        leftBudget.append(money)
                        itemCity.append(c)
                        enteredProfit.append(profit)
                        itemProfit.append(item[4])
                        itemExpensive.append(price_flag)

                else:
                    print('0 money left')
                    break
                print('All items bought')
    #upload data to google after all orders
    uploadCreatedBuyOrdersToSheets(itemName, itemInfo, totalAmount, boughtAmount, itemOrdersTotalCost, leftBudget, itemCity, itemExpensive, enteredProfit, itemProfit)
    return