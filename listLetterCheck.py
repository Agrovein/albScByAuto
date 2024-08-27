from convertListFromStrToInt import *

def deleteLettersFromNumbers(priceList):

    unletterlist = list()
    for item in priceList:
        try:
            m = float(item)
        except:
            item = ''
        unletterlist.append(item)    
    
    unletterlist[:] = [x for x in unletterlist if x]

    return convertListToInt(unletterlist)

def deleteLettersFromNumbersPrice(priceList):

    unletterlist = list()
    for item in priceList:
        try:
            m = float(item)
        except:
            item = ''
        unletterlist.append(item)    
    
    unletterlist[:] = [x for x in unletterlist if x]

    return convertListToIntPrice(unletterlist)