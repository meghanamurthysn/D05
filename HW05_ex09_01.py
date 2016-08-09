#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def count_letters(word):
	count = 0
	for letter in word:
		count += 1
	return count

def read_print():
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if count_letters(word) > 20:
			print(word)
##############################################################################
def main():
    read_print()  # Call your functions here.

if __name__ == '__main__':
    main()
