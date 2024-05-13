# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Products with prices.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dbohoyo- <dbohoyo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/13 14:55:20 by dbohoyo-          #+#    #+#              #
#    Updated: 2024/05/13 14:55:22 by dbohoyo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

supermarket = {
	'mango': 2.30,
	'avocado': 1.90,
	'tomato': 1.45,
	'strawberry': 2.30
}

print('Available products: mango, avocado, tomato, strawberry')
product = input('Which product do you want to buy? ').lower()

if product in supermarket:
	while True:
		try:
			kilograms = float(input('How many kilograms are you buying? '))
		except ValueError:
			print('Invalid input.')
		else:
			print('Your total price is', kilograms * supermarket[product], '€')
			break
else:
	print('That product is not available.')
