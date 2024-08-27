from listLetterCheck import *

def replaceCommasInInts(nonreplacedList):
    replacedList = []
    replace_dict = {"." : "", ",": ""}

    for item in nonreplacedList:
        for old, new in replace_dict.items():
            item = item.replace(old, new)
        replacedList.append(item)
    return deleteLettersFromNumbers(replacedList)

def replaceCommasAndDotsInQuality(nonreplacedList):
    replaced = ''
    replace_dict = {"." : "", ",": ""}

    for item in nonreplacedList:
        for old, new in replace_dict.items():
            item = item.replace(old, new)
        replaced += item
    return replaced

def replaceCommasInIntsPrice(nonreplacedList):
    replacedList = []
    replace_dict = {"." : "", ",": ""}

    for item in nonreplacedList:
        for old, new in replace_dict.items():
            item = item.replace(old, new)
        replacedList.append(item)
    return deleteLettersFromNumbersPrice(replacedList)