items = [
    "Adept's Bag",
    "Adept's Satchel of Insight",
    "Adept's Cape",
    "Adept's Scholar Robe",
    "Adept's Cleric Robe",
    "Adept's Mage Robe",
    "Adept's Scholar Cowl",
    "Adept's Cleric Cowl",
    "Adept's Mage Cowl",
    "Adept's Scholar Sandals",
    "Adept's Cleric Sandals",
    "Adept's Mage Sandals",
    "Adept's Mercenary Jacket",
    "Adept's Hunter Jacket",
    "Adept's Assassin Jacket",
    "Adept's Mercenary Hood",
    "Adept's Hunter Hood",
    "Adept's Assassin Hood",
    "Adept's Mercenary Shoes",
    "Adept's Hunter Shoes",
    "Adept's Assassin Shoes",
    "Adept's Soldier Armor",
    "Adept's Knight Armor",
    "Adept's Guardian Armor",
    "Adept's Soldier Helmet",
    "Adept's Knight Helmet",
    "Adept's Guardian Helmet",
    "Adept's Soldier Boots",
    "Adept's Knight Boots",
    "Adept's Guardian Boots",
    "Adept's Arcane Staff",
    "Adept's Great Arcane Staff",
    "Adept's Enigmatic Staff",
    "Adept's Cursed Staff",
    "Adept's Great Cursed Staff",
    "Adept's Demonic Staff",
    "Adept's Fire Staff",
    "Adept's Great Fire Staff",
    "Adept's Infernal Staff",
    "Adept's Frost Staff",
    "Adept's Great Frost Staff",
    "Adept's Glacial Staff",
    "Adept's Holy Staff",
    "Adept's Great Holy Staff",
    "Adept's Divine Staff",
    "Adept's Nature Staff",
    "Adept's Great Nature Staff",
    "Adept's Wild Staff",
    "Adept's Battleaxe",
    "Adept's Greataxe",
    "Adept's Dagger",
    "Adept's Dagger Pair",
    "Adept's Polehammer",
    "Adept's Great Hammer",
    "Adept's Brawler Gloves",
    "Adept's Battle Bracers",
    "Adept's Spiked Gauntlets",
    "Adept's Heavy Mace",
    "Adept's Morning Star",
    "Adept's Quarterstaff",
    "Adept's Iron-clad Staff",
    "Adept's Double Bladed Staff",
    "Adept's Spear",
    "Adept's Pike",
    "Adept's Glaive",
    "Adept's Broadsword",
    "Adept's Claymore",
    "Adept's Dual Swords",
    "Adept's Bow",
    "Adept's Warbow",
    "Adept's Longbow",
    "Adept's Heavy Crossbow",
    "Adept's Light Crossbow",
    "Adept's Tome of Spells",
    "Adept's Torch",
]

itemsMelee = [
    "Adept's Halberd",
    "Adept's Claws", 
    "Adept's Hammer",
    "Adept's Mace"
    ]
itemsRange = ["Adept's Crossbow"]
itemsOffHand = ["Adept's Shield"]

itemsAll = []
itemsAll.extend(items)
itemsAll.extend(itemsMelee)
itemsAll.extend(itemsRange)
itemsAll.extend(itemsOffHand)

itemsLen = len(itemsAll)
#print(itemsLen)
#print(itemsAll)


bmItemsPart1 = [
                "Adept's Cleric Robe",
                "Adept's Mage Robe",
                "Adept's Cleric Cowl",
                "Adept's Mage Cowl",
                "Adept's Cleric Sandals",
                "Adept's Mage Sandals",
                "Adept's Hunter Jacket",
                "Adept's Assassin Jacket",
                "Adept's Hunter Hood",
                "Adept's Assassin Hood",
                "Adept's Hunter Shoes",
                "Adept's Assassin Shoes",
                "Adept's Knight Armor",
                "Adept's Guardian Armor",
                "Adept's Knight Helmet",
                "Adept's Guardian Helmet",
                "Adept's Knight Boots",
                "Adept's Guardian Boots",
                "Adept's Great Arcane Staff",
                "Adept's Enigmatic Staff",
                "Adept's Great Cursed Staff",
                "Adept's Demonic Staff",
                "Adept's Great Fire Staff",
                "Adept's Infernal Staff",
                "Adept's Great Frost Staff",
                "Adept's Satchel of Insight"
]
bmItemsPart2 = [
                "Adept's Glacial Staff",
                "Adept's Great Holy Staff",
                "Adept's Divine Staff",
                "Adept's Great Nature Staff",
                "Adept's Wild Staff",
                "Adept's Greataxe",
                "Adept's Halberd",
                "Adept's Dagger Pair",
                "Adept's Claws",
                "Adept's Polehammer",
                "Adept's Great Hammer",
                "Adept's Battle Bracers",
                "Adept's Spiked Gauntlets",
                "Adept's Heavy Mace", #-
                "Adept's Morning Star",
                "Adept's Iron-clad Staff",
                "Adept's Double Bladed Staff",
                "Adept's Pike",
                "Adept's Glaive",
                "Adept's Claymore",
                "Adept's Dual Swords",
                "Adept's Warbow",
                "Adept's Longbow",
                "Adept's Heavy Crossbow",
                "Adept's Light Crossbow",
]
# under t4
bmItemsPart3 = [
                "Adept's Arcane Staff",
                "Adept's Cursed Staff",
                "Adept's Frost Staff",
                "Adept's Holy Staff",
                "Adept's Nature Staff",
                "Adept's Battleaxe",
                "Adept's Dagger",
                "Adept's Hammer",
                "Adept's Brawler Gloves",
                "Adept's Mace",
                "Adept's Quarterstaff",
                "Adept's Spear",
                "Adept's Crossbow",
                "Adept's Torch"
                ]

# under t3
bmItemsPart4 = [
                "Adept's Bag",
                "Adept's Cape",
                "Adept's Scholar Robe",
                "Adept's Scholar Cowl",
                "Adept's Scholar Sandals",
                "Adept's Soldier Armor",
                "Adept's Soldier Helmet",
                "Adept's Soldier Boots",
                "Adept's Fire Staff",
                "Adept's Bow",
                "Adept's Tome of Spells",
                ]
# from tier 1
bmItemsPart5 = [
                "Adept's Mercenary Jacket",
                "Adept's Mercenary Hood",
                "Adept's Mercenary Shoes",
                "Adept's Broadsword",
                "Adept's Shield",
                ]

#print(len(bmItemsPart1))
#print(len(bmItemsPart2))
#print(len(bmItemsPart3))
#print(len(bmItemsPart4))