#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	TAX_RATE = 0.15
	prix = 0
	for achat in data:
		prix += achat[INDEX_QUANTITY]*achat[INDEX_PRICE]

	taxes = prix * TAX_RATE
	prix_total = prix + taxes
	resultat = ""
	resultat += f"SOUS TOTAL {prix:>10.2f} $"
	resultat += f"\n" + f"TAXES      {taxes:>10.2f} $"
	resultat += f"\n" f"TOTAL      {prix_total:>10.2f} $"
 
	return resultat

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	TAX_RATE = 0.15
	# Trouver la longueur maximale des noms d'item.
	max_length = 0
	for item in data:
		if len(item[INDEX_NAME]) > max_length:
			max_length = len(item[INDEX_NAME])

	# Pour chaque item, formater le nom sur la longueur maximale et le prix total (qté x prix) sur 10 caractère et 2 décimales.
	result = ""
	for item in data:
		result += f"{item[INDEX_NAME]:{max_length}} {item[INDEX_QUANTITY] * item[INDEX_PRICE]: >10.2f} $" "\n"

	return result

def format_number(number, num_decimal_digits):
	pass #voir v.p.


def get_triangle(num_rows):
	A = "A"
	B = "+"
	C = " "
	border = B + B * 2 * num_rows
	triangle = B + C * (num_rows - 1) + A + C * (num_rows - 1) + B
	for i in range(1, num_rows):
		triangle += "\n" + B + C * (num_rows - 1 * i -1) + A * i + A + A * i + C * (num_rows - 1 * i - 1) + B
	return border + "\n" + triangle + "\n" + border


if __name__ == "__main__":
	purchases = [
		("chaise ergonomique", 1, 399.99),
		("g-fuel", 69, 35.99),
		("blue screen", 2, 39.99)
	]
	print(format_bill_items(purchases).strip())
	print("- - - - - - - - - - - - - - - - - - -")
	print(format_bill_total(purchases).strip())

	print("\n------------------")

	print(format_number(-1420069.0678, 2))

	print("\n------------------")

	print(get_triangle(2))
	print(get_triangle(5))
