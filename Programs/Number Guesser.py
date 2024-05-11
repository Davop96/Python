# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Number Guesser.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dbohoyo- <dbohoyo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/11 18:49:43 by dbohoyo-          #+#    #+#              #
#    Updated: 2024/05/11 18:49:43 by dbohoyo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

print('Think of a number between 1 and 100')
min_value = 1
max_value = 100

while True:
	guess = random.randint(min_value, max_value)
	print('Is your number', guess, '?')
	print('1: Yes, you guessed it')
	print('2: No, it\'s lower')
	print('3: No, it\'s higher')
	user_input = int(input('Your answer -> '))

	if user_input == 1:
		print('Great! Thanks for playing.')
		break
	elif user_input == 2:
		max_value = guess - 1
	elif user_input == 3:
		min_value = guess + 1
	else:
		print('The response should be 1, 2, or 3')

