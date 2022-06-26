try:
	from colorama import Fore
except:
	os.system("pip install colorama")
	from colorama import Fore
	os.system("cls")
import os
def Clear():
	os.system("cls")
	pass
def opengui():
	os.startfile("GUI.exe")

os.system("title App Blocker Builder  By RaidKiller Team  2022")
guivers = input(f"[?] Voulez-vous ouvrire une interface grafique(O/N) :  ")

Clear()


def nogui():

	#ie : iexplore.exe
	#edge : msedge.exe
	print(f"""{Fore.BLUE}
		 ▄▄▄       ██▓███   ██▓███      ▄▄▄▄    ██▓     ▒█████   ▄████▄   ██ ▄█▀▓█████  ██▀███  
		▒████▄    ▓██░  ██▒▓██░  ██▒   ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
		▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒   ▒██▒ ▄██▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
		░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒   ▒██░█▀  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
		 ▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░   ░▓█  ▀█▓░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
		 ▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░   ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
		  ▒   ▒▒ ░░▒ ░     ░▒ ░        ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
		  ░   ▒   ░░       ░░           ░    ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░    ░     ░░   ░ 
		      ░  ░                      ░          ░  ░    ░ ░  ░ ░      ░  ░      ░  ░   ░     
		                                     ░                  ░                               
		 ▄▄▄▄    █    ██  ██▓ ██▓    ▓█████▄ ▓█████  ██▀███                                     
		▓█████▄  ██  ▓██▒▓██▒▓██▒    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒                                  
		▒██▒ ▄██▓██  ▒██░▒██▒▒██░    ░██   █▌▒███   ▓██ ░▄█ ▒                                    
		▒██░█▀  ▓▓█  ░██░░██░▒██░    ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄                                     
		░▓█  ▀█▓▒▒█████▓ ░██░░██████▒░▒████▓ ░▒████▒░██▓ ▒██▒                                   
		░▒▓███▀▒░▒▓▒ ▒ ▒ ░▓  ░ ▒░▓  ░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░                                   
		▒░▒   ░ ░░▒░ ░ ░  ▒ ░░ ░ ▒  ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░                                   
		 ░    ░  ░░░ ░ ░  ▒ ░  ░ ░    ░ ░  ░    ░     ░░   ░                                    
		 ░         ░      ░      ░  ░   ░       ░  ░   ░                                                 
		      ░                       ░                                               
	{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.CYAN} Créé Par @RaidKiller{Fore.RESET}
________________________________________________________________________________________________________________________
	""")

	#Collect Infos
	file_name = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.CYAN} Nom Du Fichier > ")
	Clear()
	print(f"""{Fore.BLUE}
			App Blocker
			builder{Fore.RESET}
________________________________________________________________________________________________________________________

{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.CYAN} Nom Du Fichier > """ + file_name + """
	""")
	process_to_block = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.CYAN} Processus à bloquer > ")

	os.system("title App Blocker Builde - écriture du fichier (0/4)")
	Clear()
	#Build : 
	print("""

	[!] Build En cours...
________________________________________________________________________________________________________________________""")
	os.system("echo @echo off>>" + file_name + ".bat")
	print('[!] commande "@echo off" écrite')
	os.system("title App Blocker Builde - écriture du fichier (1/4)")

	os.system("echo :main>>" + file_name + ".bat")
	print('[!] étiquette ":main" placée')
	os.system("title App Blocker Builde - écriture du fichier (2/4)")

	os.system("echo taskkill /pid " + process_to_block + ">>" + file_name + ".bat")
	print('[!] Fameuse Commande pour arrêter le procesus écrite')
	os.system("title App Blocker Builde - écriture du fichier (3/4)")

	os.system("echo goto:main>>" + file_name + ".bat")
	print('[!] retour à "main"')
	os.system("title App Blocker Builde - écriture du fichier (4/4)")

	os.system("echo ::Made With App Blocker Builder>>" + file_name + ".bat")
	os.system("title App Blocker Builde - écriture terminée")
	Clear()
	print(f"""{Fore.BLUE}

			   ______             _   __        __              __   _  
			  |_   _ \           (_) [  |      |  ]            |  ] | | 
			    | |_) | __   _   __   | |  .--.| | .---.   .--.| |  | | 
			    |  __'.[  | | | [  |  | |/ /'`\' |/ /__\\/ /'`\' |  | | 
			   _| |__) || \_/ |, | |  | || \__/  || \__.,| \__/  |  |_| 
			  |_______/ '.__.'_/[___][___]'.__.;__]'.__.' '.__.;__] (_) 
	                                                          
________________________________________________________________________________________________________________________
{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.CYAN}Nous teconseillons de lancer le fichier de sortie {Fore.RED}" """ + file_name + f""" .bat"{Fore.CYAN} dans un second bureau viruel

	[Enter] Quitter
	""")
if guivers == 'o':
	opengui()
	nogui()
if guivers == 'O':
	opengui()
	nogui()

if guivers == 'n':
	nogui()
if guivers == 'N':
	nogui()