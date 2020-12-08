import os

os.chdir("Text Input")

file = open("handy_haversacks.txt","r")
rules = {}

for line in file:
    line = line.replace("\n", "")
    key = line[:line.index("bags")].replace(" ","")
    criteria = line[line.index("contain "):].replace("contain","").split(", ")
    for i in range (0,len(criteria)):
        criteria[i] = criteria[i].replace(criteria[i][criteria[i].index("bag"):],"")
        for char in criteria[i]:
            if char.isdigit():
                criteria[i] = criteria[i].replace(char,"")
        criteria[i] = criteria[i].replace(" ","")
    rules[key] = criteria

def findGold(bag):
    global rules
    if bag not in rules or bag == "noother":
        return False
    elif "shinygold" in rules[bag]:
        return True
    allGold = False
    for bagType in rules[bag]:
        gold = findGold(bagType)
        if gold == True:
            allGold = True
    return allGold
            
total = 0    
for bag in rules:
    gold = findGold(bag)
    if gold == True:
        total += 1
        
print(total)
