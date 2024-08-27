import statistics
import pyautogui
from datetime import datetime
from getRandomCoordinates import *
from getRandomDuration import *
from coordinates import *
from listComparsion import *
from convertListFromStrToInt import *
from deleteCommas import *
from dataToGoogleSheet import *
from listLetterCheck import *
from makeOrders import *
from generateAmount import *
import math

def tierListSwitch(payment):   

    averageItemList = []
    
    pyautogui.moveTo(getRandomCoordinates(buyOrderBTN_coordinates), duration=getRandomDuration())
    pyautogui.leftClick()

    fetchedPrice = fetchItemPrices(payment)

    averageItemList.append(replaceCommasInInts(fetchedPrice))

    pyautogui.moveTo(getRandomCoordinates(orderCloseBTN_coordinates), duration=getRandomDuration())
    pyautogui.leftClick()  

    return averageItemList

def BlackMarketItemWindow(tier, enchantement, tierCord, enchantementCord):

    averageItemList = []
    itemsSoldCount = []
    if tier != '4':
        pyautogui.moveTo(getRandomCoordinates(defaultItemTier), duration=getRandomDuration())
        pyautogui.leftClick()
        pyautogui.moveTo(getRandomCoordinates(tierCord), duration=getRandomDuration())
        pyautogui.leftClick()
    if enchantement != '0':
        pyautogui.moveTo(getRandomCoordinates(defaultItemEnch), duration=getRandomDuration())
        pyautogui.leftClick()
        pyautogui.moveTo(getRandomCoordinates(enchantementCord), duration=getRandomDuration())
        pyautogui.leftClick()

    fetchedItemPrice = fetchItemPrices(sellOrderFirst)
    fetchedItemCount = fetchCountAverage(tier, enchantement)
    averageItemList.append(replaceCommasInInts(fetchedItemPrice))
    itemsSoldCount.append(replaceCommasInInts(fetchedItemCount))
    print(itemsSoldCount)
    pyautogui.moveTo(getRandomCoordinates(orderCloseBTN_coordinates), duration=getRandomDuration())
    pyautogui.leftClick()

    return averageItemList, itemsSoldCount

def orderBuyOperations(paymentCords, target_amount, base_price, budget, itemName):
    print(f'Item Name: {itemName}, target amount is: {target_amount}')
    total_purchased = 0
    total_spent = 0
    price_flag = None  # Variable to store the price comparison result
    budget_exhausted = False  # Flag to indicate if the budget was exhausted

    pyautogui.moveTo(getRandomCoordinates(buyOrderBTN_coordinates), duration=getRandomDuration())
    pyautogui.leftClick()

    fetchedPrice = fetchItemPrices(paymentCords)
    singleOrderItemPrice = replaceCommasInInts(fetchedPrice)

    if singleOrderItemPrice > base_price * 1.10:
        price_flag = 'Expensive'
        print(f'Price {singleOrderItemPrice} is Higher than 120% maximum {base_price * 1.10}')

        pyautogui.moveTo(getRandomCoordinates(orderCloseBTN_coordinates), duration=getRandomDuration())
        pyautogui.leftClick()
        time.sleep(0.5)

        return total_purchased, total_spent, price_flag, budget_exhausted
    else:
        price_flag = 'Good'
        print(f'Price {singleOrderItemPrice} is Lower than 120% maximum {base_price * 1.10}')
    #amount_to_purchase = target_amount
    purchase_cost = target_amount * singleOrderItemPrice

    if purchase_cost <= budget:
        # If the total cost of the current purchase is within the remaining budget, buy the entered amount
        crBuyOrder(target_amount, singleOrderItemPrice)
        total_purchased = target_amount
        #total_spent += purchase_cost
    else:
        # If the total cost of the entered amount exceeds the remaining budget, buy as much as possible
        remaining_budget = budget
        affordable_amount = remaining_budget // singleOrderItemPrice
        crBuyOrder(affordable_amount, singleOrderItemPrice)
        print(f"Budget is insufficient. You can afford to buy only {affordable_amount} items.")
        total_purchased = affordable_amount
        #total_spent += affordable_amount * singleOrderItemPrice
        budget_exhausted = True
    orderCost = fetchItemPrices(totalCost)
    total_spent = replaceCommasInInts(orderCost)
    # Print final totals
    print(f"Final total purchased: {total_purchased}")
    print(f"Final total spent: {total_spent}")

    pyautogui.moveTo(getRandomCoordinates(createOrderBtn), duration=getRandomDuration())
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(850, 569, duration=getRandomDuration())
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(850, 570, duration=getRandomDuration())
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(850, 571, duration=getRandomDuration())
    pyautogui.leftClick()
    print(f"Total spent so far: {total_spent} and budget: {budget}")
    return total_purchased, total_spent, price_flag, budget_exhausted

def orderSellOperations():

    empty_inventory_hash, current_inventory_hash = checkInventoryEmptiness()

    #similar = 0
    
    count = 0
    while current_inventory_hash != empty_inventory_hash:
        

        qualityCordsDict = {
        'Normal': (1, qualityNormal),
        'Good': (1, qualityGood),
        'Outstanding': (2, qualityOutstanding),
        'Excellent': (2, qualityExcellent),
        'Masterpiece': (2, qualityMasterpiece)
    }

        #similar = checkInventoryEmptiness()
        time.sleep(0.2)
        pyautogui.moveTo(getRandomCoordinates(buySellBtn), duration=getRandomDuration())
        pyautogui.leftClick()
        time.sleep(0.2)
        quality = checkQuality()
        fixedQuality = (replaceCommasAndDotsInQuality(quality))
        value = qualityCordsDict.get(fixedQuality)
        #cord = value[1]

        if value[0] == 1:
            time.sleep(0.5)
            price = fetchItemPrices(sellOrderFirst)
            fixedPrice = (replaceCommasInInts(price))
            crSellOrder(fixedPrice)
            count += 1
            print(f"count {count}")
        else:
            print(f'Quality is: {fixedQuality} and changing to Good...')
            pyautogui.moveTo(getRandomCoordinates(qualityDefault), duration=getRandomDuration())
            pyautogui.leftClick()
            time.sleep(0.2)
            pyautogui.moveTo(getRandomCoordinates(qualityGood), duration=getRandomDuration())
            pyautogui.leftClick()
            price = fetchItemPrices(sellOrderFirst)
            fixedPrice = (replaceCommasInInts(price))
            time.sleep(0.2)
            pyautogui.moveTo(getRandomCoordinates(qualityDefault), duration=getRandomDuration())
            pyautogui.leftClick()
            time.sleep(0.2)
            pyautogui.moveTo(getRandomCoordinates(value[1]), duration=getRandomDuration())
            pyautogui.leftClick()
            crSellOrder(fixedPrice)
            count += 1
            print(f"count {count}")

        pyautogui.moveTo(getRandomCoordinates(createOrderBtn), duration=getRandomDuration())
        pyautogui.leftClick()
        time.sleep(0.2)
        rawr, current_inventory_hash = checkInventoryEmptiness()
    return print('done')

def fastBuyOperations(target_amount_str, base_price, budget, itemName, price_check_interval=5, price_tolerance=1.10):
    try:
        target_amount = int(target_amount_str)
    except ValueError:
        raise ValueError("Invalid input: target_amount and budget must be strings representing integers")

    total_purchased = 0
    total_spent = 0
    price_flag = None  # Variable to store the price comparison result
    budget_exhausted = False
    iteration_count = 0
    expensiveIterator = 0
    average_price = 0
    indexList = []
    price = 0
    print('Item Name:', itemName, 'Needed Amount:', target_amount)
    time.sleep(0.5)
    fetchedPrice = something()
    correctedPrice = replaceCommasAndDotsInQuality(fetchedPrice)
    price = int(correctedPrice)
    if price > round(base_price * price_tolerance):
        price_flag = 'Expensive'
        print(f'Price {price} is higher than {price_tolerance * 100}% of base price {base_price}')
        print('item to expensive even before while loop')
        return total_purchased, total_spent, price_flag, budget_exhausted
    else:
        price_flag = 'Good'
        print(f'Price {price} is within {price_tolerance * 100}% of base price {base_price}')

        while budget > 0 and total_purchased < target_amount:
            iteration_count += 1

            # Check the price at regular intervals
            if iteration_count % price_check_interval == 0:
                fetchedPrice = something()
                correctedPrice = replaceCommasAndDotsInQuality(fetchedPrice)
                price = int(correctedPrice)

                if price > round(base_price * price_tolerance):
                    price_flag = 'Expensive'
                    print(f'Price {price} is higher than {price_tolerance * 100}% of base price {base_price}')
                    break  # Exit the function if the price condition is met
                else:
                    price_flag = 'Good'
                    print(f'Price {price} is within {price_tolerance * 100}% of base price {base_price}')

            time.sleep(0.5)

            fetchItemOrderAmount = 1  # Set to purchase only 1 item per iteration
            order_cost = price * fetchItemOrderAmount

            print(f"Purchasing 1 item at average price {price}")

            if total_purchased + fetchItemOrderAmount <= target_amount:
                if total_spent + order_cost <= budget:
                    # If the total cost of the current order is within the remaining budget, buy the item
                    crFastBuyOrder()
                    print('Order total cost:', order_cost)
                    total_purchased += fetchItemOrderAmount
                    total_spent += order_cost
                else:
                    print('Budget is exhausted')
                    budget_exhausted = True
                    break  # Exit the loop since the budget is exhausted

            print(f"Total purchased so far: {total_purchased} of total amount: {target_amount}")
            print(f"Total spent so far: {total_spent} and budget: {budget}")

    return total_purchased, total_spent, price_flag, budget_exhausted

def testRecognition():
    #amount = fetchItemPrices(amountFastBuy)
    #price = checkAmountFastBuy(totalCost)
    #p = fetchItemPrices(fastBuyPrice)
    #fixedPrice = (replaceCommasInInts(amount))
    #fixedPrice = (replaceCommasInInts(price))
    #fixedPrice = (replaceCommasInInts(p))

    quality = something()
    fixedQuality = (replaceCommasAndDotsInQuality(quality))
    print(fixedQuality)
    print(type(fixedQuality))
    return

#testRecognition()