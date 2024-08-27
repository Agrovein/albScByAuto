from listComparsion import *

def convertListToInt(nonconvertedList):

    convertedList = [eval(i) for i in nonconvertedList]

    return replaceAnomalNumbers(convertedList)

def convertListToIntPrice(nonconvertedList):

    convertedList = [eval(i) for i in nonconvertedList]

    return convertedList