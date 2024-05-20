# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Socket Scanner.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dbohoyo- <dbohoyo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/13 14:55:25 by dbohoyo-          #+#    #+#              #
#    Updated: 2024/05/13 14:55:28 by dbohoyo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket

ip = input('Enter the IP address of the host you want to scan -> ')
start_port = int(input('Enter the starting port -> '))
end_port = int(input('Enter the ending port -> '))

found_ports = []

for port in range(start_port, end_port + 1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	print('Scanning port -> ', port)
	response = s.connect_ex((ip, port))
	if response == 0:
		print('Port found -> ', port)
		found_ports.append(port)
	s.close()

print('Found ports:', found_ports)

