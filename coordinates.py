import pyautogui
import time

createBuyOrderBTN_coordinates = (1481, 462, 1511, 509)
searchBar_coordinates = (494, 195, 637, 211)
revertBTN_coordinates = (656, 194, 668, 209)
buyOrderBTN_coordinates = (1305, 410, 1395, 420)

cursorMoveCorde = (1201, 530, 1438, 571)

categoryDefaultCords = (705, 195, 849, 210)
allCords = (701, 227, 857, 250)
meleeCords = (701, 665, 857, 689)
rangedCords = (702, 835, 855, 855)
offHandCords = (701, 732, 855, 756)


# list of Tier List btns coordinates in Overall Window
defaultOveralTier = (883, 196, 1035, 209)
tier4Overal = (879, 362, 1039, 383)
tier5Overal = (880, 395, 1037, 416)
tier6Overal = (879, 428, 1037, 452)
tier7Overal = (881, 461, 1035, 486)
tier8Overal = (882, 495, 1037, 514)



# list of Enchantement List btns coordinates in Overall Window
defaultOverallEnch = (1067, 197, 1202, 210)
ench0Overal = (1062, 256, 1216, 279)
ench1Overal = (1061, 292, 1218, 313)
ench2Overal = (1060, 326, 1217, 346)

EnchantmentDefaultList_coordinates = (528, 359, 658, 376)
Enchantment1List_coordinates = (524, 424, 676, 444)

#List of Quality coordinates
QualityDefaultList_coordinates = (720, 358, 858, 376)
QualityGoodList_coordinates = (714, 425, 869, 446)

#Area with listed items and prices for Sell Orders (Fast buy)
PriceListCoordinates = (1026, 333, 1101, 512)
PriceListCoordinates2 = (1036, 312, 1126, 531)
buyOrderFirst = (1337, 324, 1427, 345)
sellOrderFirst = (1030, 324, 1126, 345)
sellOrderAll = (1030, 312, 1126, 531)
#sellOrderBM = (1030, 312, 1126, 531)
#Order Window revert button coordinates
orderRevertBTN_coordinates = (908, 359, 917, 374)

#Order Window close button coordinates
orderCloseBTN_coordinates = (928, 248, 938, 264)

#Sell Orders Scroll
ordersSellScrollBTN_coordinates = (1251, 330, 1255, 388)
#basic coordinates for dragging price lists (for prices fetching)
basiccoord = (1119, 500)

# BlackMarket coordinates
# sell order window btn
sellOrdBMbtn = (1480, 359, 1516, 407)
# tiers btns
#default
defaultItemTier = (460, 358, 475, 378)
# upper tier 4
tier4ItemUpper = (460, 390, 487, 413)
tier5ItemUpper = (460, 424, 485, 448)
tier6ItemUpper = (460, 456, 485, 479)
tier7ItemUpper = (460, 492, 484, 513)
tier8ItemUpper = (460, 524, 487, 542)
# lower tier 4
tier4ItemLower = (460, 423, 488, 445)
tier5ItemLower = (460, 456, 486, 480)
tier6ItemLower = (460, 489, 488, 514)
tier7ItemLower = (460, 524, 486, 546)
tier8ItemLower = (460, 558, 485, 577)
# lower tier 3
tier4ItemThird = (460, 456, 485, 478)
tier5ItemThird = (460, 491, 486, 513)
tier6ItemThird = (460, 524, 487, 542)
tier7ItemThird = (460, 561, 486, 579)
tier8ItemThird = (460, 593, 486, 611)

tier4ItemFirst = (460, 493, 481, 509)
tier5ItemFirst = (460, 525, 483, 544)
tier6ItemFirst = (460, 558, 486, 581)
tier7ItemFirst = (460, 593, 482, 615)
tier8ItemFirst = (460, 624, 486, 643)

# enchantement btns
#default
defaultItemEnch = (527, 358, 670, 373)
ench0Item = (521, 389, 680, 411)
ench1Item = (520, 421, 679, 447)
ench2Item = (521, 457, 678, 479)
# items sold 
soldItemsCursor = (1510, 702)
#soldCountAndPriceWindow = (1293, 651, 1510, 702) # Maybe need rewrite later
#soldCountAndPriceWindow = (1293, 661, 1510, 702)
fourWeekBtn = (1007, 764) 
#anotherPoint = (1360, 670, 1406, 702) # best coordinates for T4.0
anotherPoint = (1360, 670, 1406, 695)
#secondPoint = (1293, 661, 1510, 702)
count40 = (1314, 671, 1409, 698)
count50 = (1303, 671, 1398, 700)
count60 = (1304, 671, 1398, 696)
count70 = (1303, 671, 1396, 698)
count80 = (1296, 671, 1383, 697)
zero = (1305, 671, 1395, 697)
# t4.0 309 = 1314, 671, 1409, 698
# t5.0 122 = 1303, 671, 1398, 700
# t6.0 95 = 1304, 671, 1398, 696
# t7.0 20 = 1303, 671, 1396. 698
# t8.0 3 = 1296, 671, 1383, 697
# t4.1 146 = 1305, 671, 1395, 696
# t5.1 15 = 1306, 672, 1395, 695
# t6.1 23 = 1298, 671, 1395, 696
# t7.1 1 = 1300, 672, 1386, 695

myOrderBtn = (1485, 566, 1507, 609)
myOrderCancelBtn = (1392, 373, 1399, 386)

amountOrderBuy = (480, 586)
priceOrder = (519, 655, 610, 655)

createOrderBtn = (818, 773, 912, 793)
totalCost = (468, 768, 598, 797)

acceptBuyOrderCreateBtn = (850, 571)

buySellBtn = (1305, 396, 1400, 417)
sellOrder = (457, 501, 582, 512)

emptyInve = (794, 400, 1097, 523)

qualityDefault = (717, 359, 858, 376) 
qualityNormal = (715, 389, 865, 413)
qualityGood = (714, 424, 865, 443)
qualityOutstanding = (714, 458, 868, 478)
qualityExcellent = (715, 491, 869, 510)
qualityMasterpiece = (714, 526, 867, 543)

fastBuyPrice = (1098, 390, 1234, 420)
fastBuyAmount = (804, 577, 833, 594)

#amountFastBuy = (1133, 323, 1201, 346)
#amountFastBuy = (1125, 320, 1225, 350)
amountFastBuy = (1135, 325, 1175, 345)
#amountFastBuy = (1030, 324, 1175, 345)

fastBuyCheck = (459, 465, 471, 477)