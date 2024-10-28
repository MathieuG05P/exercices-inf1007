#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text):
	nb_let = 0
	for letter in text:
		nb_let += int(letter.isalnum())
	return nb_let

def get_word_length_histogram(text):

	return text.split()
def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	word = "est?"
	print(f"The number of characters for '{word}' is: {get_num_letters(word)}")
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
