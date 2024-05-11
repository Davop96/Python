# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Multiplication tables.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dbohoyo- <dbohoyo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/11 18:49:43 by dbohoyo-          #+#    #+#              #
#    Updated: 2024/05/11 18:49:43 by dbohoyo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

while True:
	try:
		n = int(input('Enter the number for which you want to generate the multiplication table (type -1 to exit) -> '))
		if n == -1:
			break
		for i in range(11):
			print(f'{n} x {i} = {n*i}')
	except ValueError:
		print('Invalid input. Please enter a valid number.')
