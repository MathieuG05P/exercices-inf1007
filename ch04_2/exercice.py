#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
    premiernom = name.split("-")[0]
    a = premiernom.lower()
    b = a.capitalize()
    return "Bonjour" + " " + b

def get_random_sentence(animals, adjectives, fruits):
	sentence_template = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."
	animal_word = animals[random.randrange(0, len(animals))]
	adject_word = adjectives[random.randrange(0, len(adjectives))]
	fruit_word = fruits[random.randrange(0, len(fruits))]
	words = [animal_word, adject_word, fruit_word]
	return sentence_template % tuple(words)

def format_date(year, month, day, hours, minutes, seconds):
	return ""

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
