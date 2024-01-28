###__IMPORT__###

import os , time
from time import sleep

###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

logo = (f'''{GREEN}

 █████  ██████  ███    ██  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██   ██ ████   ██ 
███████ ██   ██ ██ ██  ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██   ██ ██  ██ ██ 
██   ██ ██████  ██   ████ ██   ██ ██   ████ 
                                            
 ''')

menu = ('''
[1] Basic Setup
[2] Join Gr0up
[3] Contract Me
[4] Follow Page
[5] Join Teligram
[6] Exit
''')

def setup ():
	os.system("pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4")
	
def join():
	os.system("xdg-open https://www.facebook.com/groups/741830068005520/")
	
def main():
	os.system('clear')
	print(logo)
	print('')
	print(menu)
	option = input(f'{RED}Choose Option : ')
	if option == '1':
		setup()
		main()
		
	elif option == '2':
		join()
		main()

	elif option == '3':
		os.system("xdg-open https://www.facebook.com/mdabuhurayra.adnan/")
		main()

	elif option =='4':
		os.system("xdg-open https://www.facebook.com/teamhackerno1")
		main()

	elif option =='5':
		os.system("xdg-open https://web.telegram.org/k/#@teamhackerno1")
		main()

	elif option =='6':
		exit()
	else:
		print('\n')
		print(f'Choose Carefully')
		time.sleep(3)
		main()

main()





#os.system('apt install git')
