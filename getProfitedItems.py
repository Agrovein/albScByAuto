def getProfitedItems(sheetList, cityInTable, profit):

    preparedList = sheetList[3:-1]
    cityDict = {
            '1': (6, [0, 1, 3, 4, 6], 'Thetford'),
            '2': (10, [0, 1, 3, 8, 10], 'Fort Sterling'),
            '3': (14, [0, 1, 3, 12, 14], 'Lymhurst'),
            '4': (18, [0, 1, 3, 16, 18], 'Bridgewatch'),
            '5': (22, [0, 1, 3, 20, 22], 'Martlock')}
    
    itemsList = []
    value = cityDict.get(cityInTable)
    profitId, neededItemsId, city = value[0], value[1], value[2]

    for item in preparedList:
        bufferList = []
        if int(item[profitId]) >= int(profit):
            if int(item[1]) > 1:
                if int(item[3]) > 1:
                    if int(item[neededItemsId[3]]) > 1:
                        for id in neededItemsId:
                            bufferList.append(item[id])
                        bufferList.append(city)
                        itemsList.append(bufferList)

    return itemsList