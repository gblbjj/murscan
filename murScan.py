import socket, sys, os

def scan(ip, port):
	response = sock.connect_ex((ip,port))
	if response == 0:
		return True
	else:
		return False

def banner():
	print(r"""

 ___ __ __            ______   ______   ________   ___   __      
/__//_//_/\          /_____/\ /_____/\ /_______/\ /__/\ /__/\    
\::\| \| \ \         \::::_\/_\:::__\/ \::: _  \ \\::\_\\  \ \   
 \:.      \ \         \:\/___/\\:\ \  __\::(_)  \ \\:. `-\  \ \  
  \:.\-/\  \ \  _______\_::._\:\\:\ \/_/\\:: __  \ \\:. _    \ \ 
   \. \  \  \ \/______/\ /____\:\\:\_\ \ \\:.\ \  \ \\. \`-\  \ \
    \__\/ \__\/\__::::\/ \_____\/ \_____\/ \__\/\__\/ \__\/ \__\/
                                                                 

Created by: Mur
""")


os.system('clear')
banner()
while True:
	opt = input("""\n\nWhat type of scan do you want to do?
		1)TCP Port scan
		2)UDP Port Scan
		3)Exit\n""")
	

	if opt == '1':
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip = input('\nTarget IP: ')
		sock.settimeout(0.3)
		print('\n\nPorts:')
		for port in range(10000):
			response = scan(ip, port)	
			if response:
				print('Port {}/tcp open'.format(port))

	elif opt == '2':
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(0.3)
		ip = input('\nTarget IP: ')
		print('\n\nPorts:')
		for port in range(10000):
			response = scan(ip, port)
			if response:
				print('Port {}/udp open'.format(port))

	elif opt == '3':
		print('\n\nThank you to use MScan by Mur')
		sys.exit(0)

	else:
		print('Choose a valid option!')
		print('Thank you to use MScan by Mur')
		sys.exit(1)
