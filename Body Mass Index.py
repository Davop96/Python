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
		weight = float(input('Enter your weight here in kg -> '))
		height = float(input('Enter your height here in m -> '))
		if weight <= 0 or height <= 0:
			raise ValueError("Weight and height must be positive values.")
		bmi = weight / height**2
		bmi = round(bmi, 2)
		if bmi <= 0:
			raise ValueError("Calculating BMI is not possible.")
		if bmi < 18.5:
			print(f'Your BMI is {bmi}: You are underweight, consider gaining weight.')
		elif 18.5 <= bmi < 25:
			print(f'Your BMI is {bmi}: You have a normal weight, keep it up!')
		else:
			print(f'Your BMI is {bmi}: You are overweight, consider a diet.')
		break
	except ValueError as e:
		print(f'Error: {e}')


  