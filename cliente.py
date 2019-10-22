import socket, time, sys

def Cliente(HOST, PORT):

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)
	tcp.connect(dest)

	print('Para sair digite desconectar!')
	print('Digite a requisição desejada:')
	print('1 - \\autores: retorna o nome dos autores do trabalho.')
	print('2 - \\trendmusic: retorna as músicas mais populares do momento do youtube.')
	print('3 - \\music <nome da música> : retorna a URL na música desejada.')
	msg = input()

	while msg != 'desconectar':
		
		if msg == '\\autores':
			
			print('Aguardando resposta....')
			tcp.send(msg.encode())
			time.sleep(2)
			resp = tcp.recv(1024)
			print('Resposta: ', resp.decode())

		elif msg == '\\trendmusic':
			
			print('Aguardando resposta....')
			tcp.send(msg.encode())
			time.sleep(2)
			resp = tcp.recv(1024)
			print('Resposta = ', resp.decode())

		elif len(msg) > 7 and msg[0:7] == '\\music ':
			
			print('Aguardando resposta....')
			tcp.send(msg[7:].encode())
			time.sleep(2)
			resp = tcp.recv(1024)
			print('Resposta = ', resp.decode())
		
		else:

			print('Requisição não existe! Tente um existente!')
		
		time.sleep(1)
		print()
		print ('Para sair digite desconectar!')
		print('Digite a requisição desejada:')
		print('1 - \\autores: retorna o nome dos autores do trabalho.')
		print('2 - \\trendmusic: retorna as músicas mais populares do momento do youtube.')
		print('3 - \\music <nome da música> : retorna a URL na música desejada.')
		msg = input()

	print('Desconectado!')

	tcp.close()