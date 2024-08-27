import time
import datetime
import gspread

budget = 16234
itemOrderPrice = 15339
price = 3069

def mins(neededAmount, orderAmount):
    if neededAmount - orderAmount > 0:
        result = orderAmount
    else:
        result = orderAmount-abs(neededAmount-orderAmount)
    print(result)
    return result

#res = mins(15, 2)

def budgetCalculations(amount, totalBudget, currentItemBudget, itemprice):
    newAmount = 1
    ordercost = 0
    if itemprice*amount > totalBudget - currentItemBudget:
        iterator = 1
        while iterator < amount:
            if itemprice * iterator < totalBudget - currentItemBudget:
                newAmount = iterator
                ordercost += itemprice * iterator
            iterator += 1
        print('newAMount: ', newAmount)
        #print(ordercost)   
    return

#budgetCalculations(res, budget, itemOrderPrice, price)

total = 100
bought = 0
itemCost = 0

while bought <= total:
    #order = 80
    if bought + orderAmount > total:
        amount = total - bought
        
        #buy order
        bought += amount
        itemCost += orderCost*amount
    else:
        #buy order
        bought += orderAmount
        itemCost += orderCost*orderAmount
    if itemCost > budget
    print()

'''
bought = 5
needed = 5
orderAmount = 3
result = needed - orderAmount
totalBudget = 510000
itemBudget = 15339
cost = 205325
orderCost = 0
i = 1
amount = 0
while i < needed:
    if cost*i < totalBudget - itemBudget:
        if result < 0:
            print('negative')
            amount = i+1
            orderCost = cost*i+cost
        print('negative with good budget')
        amount = i
        orderCost = cost*i
    else:
        print('positive with bad budget')
        amount = i
        orderCost = cost*i
    i += 1
#if needed - orderAmount < 0:
    #amount += 1 
print('order Amount: ', amount)
print('order Cost: ', cost*(amount))
print('order Cost + Item Budget: ', cost*(amount)+itemBudget)
print('order Cost + Item Budget + 1 item cost: ', cost*(amount+1)+itemBudget+cost)

'''



'''
cityDict = {
    '1': (6, [0, 1, 3, 4, 6], 'Thetford'),
    '2': (10,[0, 1, 3, 8, 10], 'Fort Sterling'),
    '3': (14,[0, 1, 3, 12, 14], 'Lymhurst'),
    '4': (18,[0, 1, 3, 16, 18], 'Bridgewatch'),
    '5': (22,[0, 1, 3, 20, 22], 'Martlock')}

cityInTable = '5'

list_of_lists = worksheet.get_all_values()
profit = '300'
slicedList = list_of_lists[2:]
#print(slicedList)
itemsList = []
value = cityDict.get(cityInTable)
profitId, neededItemsId, city = value[0], value[1], value[2]

for item in slicedList:
    bufferList = []
    if int(item[profitId]) >= int(profit):
        if int(item[1]) > 1:
            if int(item[3]) > 1:
                if int(item[neededItemsId[3]]) > 1:
                    for id in neededItemsId:
                        bufferList.append(item[id])
                    bufferList.append(city)
                    itemsList.append(bufferList)

    
for i in itemsList:
    print(i)

'''