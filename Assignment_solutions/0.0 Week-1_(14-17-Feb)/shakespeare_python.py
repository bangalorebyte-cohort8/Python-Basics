#!usr/bin/env python3.6
import random

string = "methinks it is like a weasel"



def generate_27(n):
	alphabet = "abcdefghijklmnopqrtsuvwxyz "
	empty_string= "" #accumalator
	for i in range(n):
		# pick an index number between 0 and 26
		empty_string += alphabet[random.randrange(27)]
	return empty_string	

def score(target,test_string):
	same_chars = 0
	percentage = same_chars/len(target)
	for i in range(len(target)):
		if target[i] == test_string[i]:
			same_chars += 1
	return percentage

#print(score(string,generate_27(28)))

def keep_looking():
	new_string = generate_27(28)
	best = 0
	new_score = score(string,new_string)
	while new_score < 1:
		if new_score > best:
			print(new_score,new_string)
			best = new_score
		new_string = generate_27(28)
		new_score = score(string,new_string)
	
keep_looking()