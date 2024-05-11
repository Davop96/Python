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
		grade = float(input('Enter your grade to see if you passed or not -> '))
	except ValueError:
		print('Sorry, only numbers are accepted. Please enter a valid grade.')
	else:
		if grade < 0 or grade > 10:
			print('Invalid input. Grades must be between 0 and 10.')
		else:
			if grade < 5:
				print('You failed miserably.')
			elif grade < 7:
				print('You passed, but just barely.')
			elif grade < 9:
				print('Well done! Your performance is noteworthy.')
			else:
				print('Outstanding! You nailed it.')
			break
