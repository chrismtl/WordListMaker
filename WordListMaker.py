#!/usr/bin/python3
import os

YES = "y"
NO = "n"
SUCCESS = "s"
FAIL = "f"
text_S = "success"
text_F = "fail"
text = {SUCCESS:text_S , FAIL:text_F}

DISPLAY     = "Display wordlist? (y/n): "
SAVE        = "Save wordlist? (y/n): "
COMPILE     = "Program (success => s / fail => f): "
ENTRY_ERROR = "Invalid entry, please try again"

t1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","N","o","p","q","r","s","t","u","v","w","x","Y","z"]
t2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
t3 = ["0","1","2","3","4","5","6","7","8","9"]
t4 = ["-","_","*","&","!","?","#"]

table = {"a":t1 , "A":t2 , "N":t3 , "&":t4}
name = {"a":"Minsucule " , "A":"Majuscule " , "N":"Chiffre   " , "&":"Symbole   "}

def clear():
	t = ""
	t = str(os.system("clear"))
	print(t[:0])

def title():
	clear()
	print(" __    __              _     __ _     _    ")
	print("/ / /\ \ \___  _ __ __| |   / /(_)___| |_  ")
	print("\ \/  \/ / _ \| '__/ _` |  / / | / __| __| ")
	print(" \  /\  / (_) | | | (_| | / /__| \__ \ |_  ")
	print("  \/  \/ \___/|_|  \__,_| \____/_|___/\__| ")
	print("              _                            ")
	print("  /\/\   __ _| | _____ _ __                ")
	print(" /    \ / _` | |/ / _ \ '__|               ")
	print("/ /\/\ \ (_| |   <  __/ |                  ")
	print("\/    \/\__,_|_|\_\___|_|                  \n")

def thanks():
	clear()
	print(" _____ _                 _         ")
	print("/__   \ |__   __ _ _ __ | | _____  ")
	print("  / /\/ '_ \ / _` | '_ \| |/ / __| ")
	print(" / /  | | | | (_| | | | |   <\__ \ ")
	print(" \/   |_| |_|\__,_|_| |_|_|\_\___/ ")
	print("\nfor using WordListMaker!!! :p")
                                  

def main():
	title()

	menu()

	WriteLog()

	Finish()

def menu():
	action = ""
	print("\n")
	print("1) Create wordlist")
	print("2) Crack handshake\n")

	while True:
		if action=="1" or action =="2":
			break
		elif action!="":
			print(ENTRY_ERROR)

		action = input("Action: ")

	print("\n")
	if action=="1":
		Create_wordlist()
	else:
		Crack_handshake()

def WriteIn(wordlist,textFile):
	for password in wordlist:
		textFile.write(password+"\n")

	wordlist.clear()
	textFile.close()

def Display():
	display = ""
	while display !=YES and display!=NO:
		display = input(DISPLAY)
	if display==YES:
		print(os.system("cat wordlist.txt"))

def check_or_create(directory):
	if os.system("cd "+directory)!="":
			os.system("mkdir "+directory)
			print("== Creating new '"+directory+"' directory ==\n")

def Save():
	test = ""
	while test != YES and test!= NO:
		test = input(SAVE)
	if test==YES:
		print()
		wordlist_name = input("Wordlist name : ")
		rename_command = "mv wordlist.txt "+wordlist_name+".txt"
		moove_command   = "mv "+wordlist_name+".txt Saved_wordlists"

		os.system(rename_command)
		check_or_create("Saved_wordlists")
		os.system(moove_command)

		#os.system("mv "+wordlist_name+".txt "+"~/Saved_wordlists")
		print("== wordlist saved with success!! ==\n")

	elif test==NO:
		os.system("rm wordlist.txt")
		print()
		print("=Wordlist deleted=")
		print()

def writeBlankLog():
	log = open('log.txt','w+')
	log.write("-----------------------\n")
	log.write("| ==COMPILE==STATS=== |\n")
	log.write("|Compile success : 000|\n")
	log.write("|Compile fails   : 000|\n")
	log.write("-----------------------\n")
	log.close()

def WriteLog():
	#Get compile stat
	compile_status = ""
	t = 0
	while compile_status!=SUCCESS and compile_status!=FAIL:
		if t!=0: print(ENTRY_ERROR)
		compile_status = input(COMPILE)
		t+=1

	#Read store and update current compile stat on log.txt
	try:
		log = open('log.txt','r')
	except:
		writeBlankLog()
		log = open('log.txt','r')

	lines = log.readlines()

	if compile_status==SUCCESS:
		nb_s = str(int(lines[2][19:22]) + 1)
		nb_s = (3 - len(nb_s))*"0" + nb_s
		lines[2] = lines[2][:19] + nb_s + "|\n"

	else:
		nb_f = str(int(lines[3][19:22]) + 1)
		nb_f = (3 - len(nb_f))*"0" + nb_f
		lines[3] = lines[3][:19] + nb_f + "|\n"

	#Overwrite new stat on log.txt
	os.remove("log.txt")
	log = open('log.txt','w+')
	log.writelines(lines)
	log.close()

def Finish():
	back_to_menu = ""
	while True:
		if back_to_menu==YES or back_to_menu==NO:
			break
		back_to_menu = input("Back to menu? (y/n): ")

	if back_to_menu==YES:
		main()
	else:
		thanks()
		input("\nPress Enter to exit")
		os.system("clear")

def Create_wordlist():
	global wordlist
	global textFile
	wordlist = []
	textFile = open('wordlist.txt','w+')

	#Choose mode:
	print("Create your own customized wordlist!\n")
	print("1) Low custom    => predefined keywords, order combination")
	print("2) Medium custom => words and symbol combination")
	print("3) Full custom   => complete dictionnary\n")
	
	mode  = input("Wordlist type: ")
	while mode!="1" and mode !="2" and mode!="3":
		if mode=="": print("Please chose a mode")
		else: print("Incorrect entry, try again")
		mode = input("Wordlist type: ")

	#Fill wordlist:
	if mode=="1":
		low_combinations()
	elif mode=="2":
		medium_combinations()
	else:
		custom_combinations()

	WriteIn(wordlist,textFile)

	Display()

	Save()

def combinatoire(List, password, wordlist, taille):
	s = len(List)
	
	if s>taille:
		for i in range(0,s):
			item = List[i]
			subPassword=password + item
			subList = List.copy()
			subList.remove(item)
			combinatoire(subList, subPassword, wordlist, taille)
	elif s==taille:
		for item in List:
			finalPassword = password + item
			wordlist.append(finalPassword)

def add_simple_combinations(List,wordlist):
	for i in range(0,len(List)):
		n = len(List)-i
		combinatoire(List,"",wordlist,n)

def add_bloc_combinations(List,password,bloc):
	#print(bloc,nb_bloc)
	l = len(List)-1
	for item in List[bloc]:
		subPassword =  password + item
		if bloc!=l:
			add_bloc_combinations(List, subPassword, bloc+1)
		else:
			wordlist.append(subPassword)

def check_composition(composition, dictionnary):
	nb_char = len(composition)

	for i in range(0,nb_char):
		char = composition[i]
		if dictionnary.count(char)==0: return False

	return True

def low_combinations():
	print()
	print("Enter here any pre-defined keywords (word, number or special character)")
	print()
	keyword = ""
	k = 0
	keywordList=[]
	
	print("Keywords:")
	while True:
		keyword = input()
		if keyword=="": break
		keywordList.append(keyword)
	
	add_simple_combinations(keywordList,wordlist)

def medium_combinations():
	rankList = ["High","Medium","Low"]
	preBlocList = [[],[],[]]

	for i in range(0,3):
		print(rankList[i],"Bloc: ")
		while True:
			item_in_bloc = input()
			if item_in_bloc=="": break
			preBlocList[i].append(item_in_bloc)

	
	Bloc0 = [""] + preBlocList[1] 
	Bloc1 = preBlocList[0]
	Bloc2 = [""] + preBlocList[1]
	Bloc3 = []
	add_simple_combinations(preBlocList[2],Bloc3)
	Bloc3 = [""] + Bloc3

	blocList = [Bloc0, Bloc1, Bloc2, Bloc3]
	add_bloc_combinations(blocList,"",0)

def custom_combinations():
	Names = table.keys()
	print("-----------------")
	print("|Char symbols:  |")
	for item in Names:
		print("|"+item+" => "+name[item]+"|")
	print("-----------------\n")

	check = False
	composition = ""
	dictionnary = []
	for item in table.keys():
		dictionnary.append(item)
	while not check:
		if composition!="": print("\n"+ENTRY_ERROR+"\n")
		composition = input("Enter here your composition: ")
		check = check_composition(composition, dictionnary)

	blocList=[]
	l = len(composition)
	for i in range(0,l):
		char = composition[i]
		blocList.append(table[char])

	add_bloc_combinations(blocList,"",0)

def Crack_handshake():
	print("======================================================================")
	print("|CRACKING|")
	print("==========")

	wordlist_path  = input("Drop here wordlist  : ")
	handshake_path = input("Drop here handshake : ")

	check_or_create("Handshakes")

	copy_command = "cp "+handshake_path+" Handshakes"
	crack_command = "aircrack-ng "+handshake_path+" -w "+ wordlist_path

	os.system(copy_command)
	print(os.system(crack_command))

if __name__ == "__main__":
	main()
