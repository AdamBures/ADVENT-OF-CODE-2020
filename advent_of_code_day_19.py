import re
import os

os.chdir("Text input")

with open('monster_messages.txt', 'r') as file:
	files = file.readlines()
rules = {}

def matchLines(tLine):
	tLine = tLine.strip()
	ans = re.search(checkRule,tLine)	
	if ans: 
		if ans.start() == 0 and ans.end() == len(tLine):
			return 1
		else: 
			return 0
	else: 
		return 0
	
matches = 0
for line in files:
	if line[0].isdigit():
		line = line.strip()
		ruleSet = line.split(": ")
		rules[ruleSet[0]] = ruleSet[1]
		if rules[ruleSet[0]].find("|") > -1: rules[ruleSet[0]]="( "+rules[ruleSet[0]]+" )"
	elif line == "\n":
		tokens = rules["0"].split(" ")
		k = 0
		while any(item.isdigit() for item in tokens):
			for token in tokens:
				if token.isdigit():
					tIndex = tokens.index(token)
					newTokens = rules[token].split(" ")
					tokens.pop(tIndex)
					for newToken in range(len(newTokens)): tokens.insert(tIndex+newToken, newTokens[newToken]);
			if k >10000: print ("Breaking at 10k..."); break
			k+=1
		checkRule = ""
		for token in tokens:
			if token.find('"') >= 0: token = token.replace('"','')
			checkRule += token		
	elif line[0] in 'ab': matches += matchLines(line)
print (matches)
