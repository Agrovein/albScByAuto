import pyautogui
import keyboard
import time
from getRandomCoordinates import *
from getRandomDuration import *
from listOfAll_Items import *
from ItemOperations import *
from coordinates import *
from dataToGoogleSheet import *
from listGeneration import *


def royalScan(tier, enchantment, city, payment):

    start = time.time()

    tierList = []
    enchList = []
    payList = []
    if len(tier) > 1:
        tierList.extend(tier)
    else:
        tierList.extend(tier)
    if len(enchantment) > 1:
        enchList.extend(enchantment)
    else:
        enchList.extend(enchantment)
    if len(payment) > 1:
        payList.extend(payment)
    else:
        payList.extend(payment)

    pyautogui.moveTo(getRandomCoordinates(createBuyOrderBTN_coordinates), duration=getRandomDuration())
    pyautogui.leftClick()
    
    for p in payList:
        dataPayments = {'1': sellOrderAll,
                        '2': buyOrderFirst}
        
        if p in dataPayments:
                paymentCord = dataPayments.get(p)

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
                pyautogui.moveTo(getRandomCoordinates(categoryDefaultCords), duration=getRandomDuration())
                pyautogui.leftClick()
                pyautogui.moveTo(getRandomCoordinates(allCords), duration=getRandomDuration())
                pyautogui.leftClick()
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

                allItemsPriceList = []
                iterator = 1
                for item in itemsAll:
                    print(item)
                    if iterator == 76:
                        pyautogui.moveTo(getRandomCoordinates(categoryDefaultCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                        pyautogui.moveTo(getRandomCoordinates(meleeCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                    if iterator == 80:
                        pyautogui.moveTo(getRandomCoordinates(categoryDefaultCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                        pyautogui.moveTo(getRandomCoordinates(rangedCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                    if iterator == 81:
                        pyautogui.moveTo(getRandomCoordinates(categoryDefaultCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                        pyautogui.moveTo(getRandomCoordinates(offHandCords), duration=getRandomDuration())
                        pyautogui.leftClick()
                    pyautogui.moveTo(getRandomCoordinates(revertBTN_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
                    pyautogui.moveTo(getRandomCoordinates(searchBar_coordinates), duration=getRandomDuration())
                    pyautogui.leftClick()
                    keyboard.write(item)       
                    time.sleep(1)
                    averageItemPricesList = tierListSwitch(paymentCord)
                    allItemsPriceList.extend(averageItemPricesList)
                    iterator += 1
                print(len(allItemsPriceList))
                uploadData(allItemsPriceList, t, e, city, p)
                            
    end = time.time()     
    print("Time elapsed: ", end - start)

def blackMarketScan(tier, enchantment, part):

    start = time.time()

    tierList = []
    enchList = []

    if len(tier) > 1:
        tierList.extend(tier)
    else:
        tierList.extend(tier)
    if len(enchantment) > 1:
        enchList.extend(enchantment)
    else:
        enchList.extend(enchantment)


    dataEnchantements = {
                        '0': ench0Item,
                        '1': ench1Item,
                        '2': ench2Item}

    if part == '1' or part == '2':
        dataTiers = {
                    '4': tier4ItemUpper,
                    '5': tier5ItemUpper,
                    '6': tier6ItemUpper,
                    '7': tier7ItemUpper,
                    '8': tier8ItemUpper}
        if part == '1':
            itemList = bmItemsPart1
        if part == '2':
            itemList = bmItemsPart2
        
    if part == '3':
        dataTiers = {
                    '4': tier4ItemLower,
                    '5': tier5ItemLower,
                    '6': tier6ItemLower,
                    '7': tier7ItemLower,
                    '8': tier8ItemLower}
        itemList = bmItemsPart3
        
    if part == '4':
        dataTiers = {
                    '4': tier4ItemThird,
                    '5': tier5ItemThird,
                    '6': tier6ItemThird,
                    '7': tier7ItemThird,
                    '8': tier8ItemThird}
        itemList = bmItemsPart4
    if part == '5':
        dataTiers = {
                    '4': tier4ItemFirst,
                    '5': tier5ItemFirst,
                    '6': tier6ItemFirst,
                    '7': tier7ItemFirst,
                    '8': tier8ItemFirst}
        itemList = bmItemsPart5

    pyautogui.moveTo(getRandomCoordinates(sellOrdBMbtn), duration=getRandomDuration())
    pyautogui.leftClick()

    for e in enchList:

        if e in dataEnchantements:
            enchantementCord = dataEnchantements.get(e)

        for t in tierList:
            
            allItemsPriceList = []
            allItemsCount = []

            if t in dataTiers:
                tierCord = dataTiers.get(t)

            for item in itemList:
                pyautogui.moveTo(getRandomCoordinates(revertBTN_coordinates), duration=getRandomDuration())
                pyautogui.leftClick()
                pyautogui.moveTo(getRandomCoordinates(searchBar_coordinates), duration=getRandomDuration())
                pyautogui.leftClick()
                keyboard.write(item)
                time.sleep(1)
                pyautogui.moveTo(getRandomCoordinates(buyOrderBTN_coordinates), duration=getRandomDuration())
                pyautogui.leftClick()

                averageItemPricesList, itemCountAndAverage = BlackMarketItemWindow(t, e, tierCord, enchantementCord)
                allItemsPriceList.extend(averageItemPricesList) 
                allItemsCount.extend(itemCountAndAverage)
            
            print(allItemsCount)
            uploadBmData(allItemsPriceList, allItemsCount, t, e, part)

    end = time.time()
    print("Time elapsed: ", end - start)
    return