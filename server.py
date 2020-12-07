import socket
import _thread


def main():
	host = '0.0.0.0'
	port = 5555
	users = 4

	s = socket.socket()
	s.bind((host, port))
	s.listen(users)
	print('Listening for connections')

	conns = []
	connecting = False

	def connUsers():
		for user in range(users):
			conn, addr = s.accept()
			conns.append(conn)
			connecting = True
			print(addr, 'connected')
			for each in range(len(conns)):
				_thread.start_new_thread(sendData, (each, ))
			connecting = False
			_thread.start_new_thread(connUsers, ())

	def sendData(user):
		while True:
			data = conns[user].recv(1024).decode('utf-8')
			for each in range(len(conns)):
				conns[each].send((data).encode('utf-8'))
			if not data or connecting:
				break
		print('Closing connections')
		s.close()


	_thread.start_new_thread(connUsers, ())

	while True:
		pass


if __name__ == '__main__':
	main()
