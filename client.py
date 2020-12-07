import socket
import _thread
import os

os.system('')

def main():
	host = '192.168.0.108'
	port = 5555

	for x in range(70):
		print('')

	try:
		file = open('config.txt', 'r+')
		write = False
	except:
		file = open('config.txt', 'w')
		write = True

	if not write:
		lines = file.readlines()
		un = lines[0][:-1]
		colour = lines[1]
	else:
		un = input('\033[2;32;40mPlease pick a username:\033[0m ')
		file.write(un + '\n')
		while True:
			try:
				print("""Pick a colour:
\033[1;30;40m30 - Black
\033[1;31;40m31 - Red
\033[1;32;40m32 - Green
\033[1;33;40m33 - Yellow
\033[1;34;40m34 - Blue
\033[1;35;40m35 - Purple
\033[1;36;40m36 - Cyan
\033[1;37;40m37 - White\033[0m""")
				colour = int(input())
				if colour:
					break
			except:
				print('\033[2;31;40mERROR: Colour must be an integer between 30 and 37\033[0m')
		file.write(str(colour))
	file.close()

	s = socket.socket()
	s.connect((host, port))

	def getMessages():
		while True:
			data = s.recv(1024).decode('utf-8')
			print(data)
	def sendMessage():
		while True:
			msg = input("Enter the message: ")
			small_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
							  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			big_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
							'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			small_ua_alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м',
								 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
			big_ua_alphabet = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н',
							   'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']
			number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

			key = 3
			cipher = ""
			plain = ""

			for i in msg:
				if i in big_alphabet:
					cipher += big_alphabet[(big_alphabet.index(i) + key) % len(big_alphabet)]
				elif i in small_alphabet:
					cipher += small_alphabet[(small_alphabet.index(i) + key) % len(small_alphabet)]
				elif i in small_ua_alphabet:
					cipher += small_ua_alphabet[(small_ua_alphabet.index(i) + key) % len(small_ua_alphabet)]
				elif i in big_ua_alphabet:
					cipher += big_ua_alphabet[(big_ua_alphabet.index(i) + key) % len(big_ua_alphabet)]
				elif i in number:
					cipher += number[(number.index(i) + key) % len(number)]
				else:
					cipher += i
			for i in cipher:
				if i in big_alphabet:
					plain += big_alphabet[(big_alphabet.index(i) - key) % len(big_alphabet)]
				elif i in small_alphabet:
					plain += small_alphabet[(small_alphabet.index(i) - key) % len(small_alphabet)]
				elif i in small_ua_alphabet:
					plain += small_ua_alphabet[(small_ua_alphabet.index(i) - key) % len(small_ua_alphabet)]
				elif i in big_ua_alphabet:
					plain += big_ua_alphabet[(big_ua_alphabet.index(i) - key) % len(big_ua_alphabet)]
				else:
					plain += i
			
			s.send(('\033[1;' + str(colour) + ';40m' + un + ':\033[0m '  + cipher).encode('utf-8'))

	_thread.start_new_thread(getMessages, ())
	_thread.start_new_thread(sendMessage, ())

	while True:
		pass

if __name__ == "__main__":
	main()
