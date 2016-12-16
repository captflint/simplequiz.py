#!/usr/bin/python3

# simplequiz.py - A Simple Quiz
# Written in 2016 by James F. Stephenson - c4p7.fl1n7@gmail.com
# To the extent possible under law, the author(s) have dedicated all 
# copyright and related and neighboring rights to this software to 
# the public domain worldwide. This software is distributed without 
# any warranty.

# You should have received a copy of the CC0 Public Domain 
# Dedication along with this software. If not, see 
# <http://creativecommons.org/publicdomain/zero/1.0/>.

import sys
import random


f = open(sys.argv[-1])
cardtext = f.read()

yn = "a"
while yn not in "YyNn":
	yn = input("Reversible cards? ")
	if yn in "Yy":
		reverse = True
	elif yn in "Nn":
		reverse = False

cards = []
card = []
side = ""

for char in cardtext:
	if char not in ":\n":
		side += char
	elif char == ":":
		card.append(side)
		side = ""
	else:
		card.append(side)
		if len(card) > 1:
			cards.append(card)
		card = []
		side = ""

wronglist = []
highestwrong = 0
def addtowrong(wrong):
	global wronglist
	global highestwrong
	notinlist = True
	for entry in wronglist:
		if entry[1] is wrong:
			notinlist = False
			entry[0] += 1
			if entry[0] > highestwrong:
				highestwrong = entry[0]
	if notinlist:
		wronglist.append([1, wrong])
		if highestwrong == 0:
			highestwrong = 1

wrong = 0
total = len(cards)
random.shuffle(cards)
while len(cards) > 0:
	card = cards.pop()
	print("\n" * 50)
	if reverse:
		random.shuffle(card)
	print(str(len(cards) + 1) + " remaining. ")
	input(card[0])
	print(card[1])
	answer = input("If wrong, enter any character and press return, if right just press return. ")
	if len(answer) > 0:
		addtowrong(card[0])
		cards.append(card)
		random.shuffle(cards)
		wrong += 1

def grade(score):
	if score <= 0:
		return("T - Troll")
	elif score < 60:
		return("D - Dreadful")
	elif score < 80:
		return("P - Poor")
	elif score < 95:
		return("A - Acceptable")
	elif score < 100:
		return("E - Exceeds Expectations")
	else:
		return("O - Outstanding!")

print("\n" * 50)
score = int((total - wrong) / total * 100)
x = 1
while x < highestwrong + 1:
	for entry in wronglist:
		if entry[0] == x:
			print(entry[0], entry[1])
	x += 1
print("Your score:", score, grade(score))

