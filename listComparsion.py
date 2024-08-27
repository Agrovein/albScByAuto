from statistics import mean

def replaceAnomalNumbers(priceList):

    if len(priceList) > 0:
        priceList.sort()

        try:
            avg = round(mean(priceList))
        except:
            avg = 1 
        

        first = priceList[0]
        last = priceList[len(priceList)-1]
        
        difference = last - first
        
        coef = 6
        
        median = difference - difference / coef
        average = 0
        if not(first<avg - avg / 2 and last > avg + avg / 2):
            average = avg
        else:
            notNormalNumberCount = 0
            replacedList = []
            for item in priceList:
                if not(item < (avg - median / coef)  or item > (avg + median / coef)):
                    replacedList.append(item)
                else:
                    notNormalNumberCount += 1
                    print(item, " not normal number")
            if notNormalNumberCount == len(priceList):
                replacedList.append(first)

                try:
                    average = round(mean(replacedList))
                except:
                    average = 1 

        return average
    else:
        average = 1
        return average 
    
def replaceAnomalNumbersInPricelist(priceList):

    if len(priceList) > 0:
        priceList.sort()

        try:
            avg = round(mean(priceList))
        except:
            avg = 1 
        

        first = priceList[0]
        last = priceList[len(priceList)-1]
        
        difference = last - first
        
        coef = 6
        
        median = difference - difference / coef
        average = 0
        if not(first<avg - avg / 2 and last > avg + avg / 2):
            average = avg
        else:
            notNormalNumberCount = 0
            replacedList = []
            for item in priceList:
                if not(item < (avg - median / coef)  or item > (avg + median / coef)):
                    replacedList.append(item)
                else:
                    notNormalNumberCount += 1
                    print(item, " not normal number")
            if notNormalNumberCount == len(priceList):
                replacedList.append(first)

                try:
                    average = round(mean(replacedList))
                except:
                    average = 1 

        return average
    else:
        average = 1
        return average 