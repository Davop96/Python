# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Body Mass Index.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dbohoyo- <dbohoyo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/11 18:49:43 by dbohoyo-          #+#    #+#              #
#    Updated: 2024/05/11 18:49:43 by dbohoyo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

while True:
	try:
		print('Enter the dividend and the divisor')
		dividend = float(input('Dividend: '))
		divisor = float(input('Divisor: '))
		result = dividend / divisor
		print('Result:', result)
		break
	except ValueError:
		print('You must enter a valid number.')
	except ZeroDivisionError:
		print('The divisor cannot be zero.')
	except Exception as e:
		print(f'An unexpected error occurred: {e}')

