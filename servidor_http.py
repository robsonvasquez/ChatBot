import socket, ssl, json

def Servidor_HTTP(requisicao, con):
	
	http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	http = ssl.wrap_socket(http, ssl_version = ssl.PROTOCOL_SSLv23)
	http.connect(('www.googleapis.com', 443))

	aux = ''
	aux1 = ''
	aux2 = ''
	aux3 = ''

	if (requisicao == '\\trendmusic'):

		msg = ('GET /youtube/v3/playlistItems?part=snippet&maxResults=1&playlistId=PL4fGSI1pDJn6puJdseH2Rt9sMvt9E2M4i&key=[SUA_CHAVE_API] HTTP/1.1\r\nHost:')
		msg = msg + '{}\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n\r\n'.format('www.googleapis.com')
		http.send(msg.encode())
		resp = http.recv(4024)
		
		while True:
			
			resp = http.recv(4024)
			aux = aux + resp.decode()
			par_a = aux.count('{')
			par_f = aux.count('}')
			if par_a == par_f:
				break
		
		filtro = json.loads(aux)
		aux1 = filtro["items"][-1]["snippet"]["title"]
		aux2 = filtro["items"][-1]["snippet"]["resourceId"]["videoId"]
		aux3 = 'Nome da música: ' + aux1 + ' Link: www.youtube.com/watch?v=' + aux2 + '&list=PL4fGSI1pDJn6puJdseH2Rt9sMvt9E2M4i'
		con.send(aux3.encode())
		
	else:
		cont = requisicao.count(' ')

		if(cont == 0):

			msg = ('GET /youtube/v3/search?part=snippet&maxResults=1&order=relevance&q=' + requisicao + '&type=video&key=AIzaSyC-J7hOChKnEqONu7i2GH2tCLUZCUgpFJY HTTP/1.1\r\nHost:')
			msg = msg + '{}\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n\r\n'.format('www.googleapis.com')
			http.send(msg.encode())
			resp = http.recv(4024)
		else:
		
			troca = requisicao.replace(' ','%20')
			msg = ('GET /youtube/v3/search?part=snippet&maxResults=1&order=relevance&q=' + troca +  '&type=video&key=AIzaSyC-J7hOChKnEqONu7i2GH2tCLUZCUgpFJY HTTP/1.1\r\nHost:')
			msg = msg + '{}\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n\r\n'.format('www.googleapis.com')
			http.send(msg.encode())
			resp = http.recv(4024)
			
		while True:

			resp = http.recv(4024)
			aux = aux + resp.decode()
			par_a = aux.count('{')
			par_f = aux.count('}')
			if par_a == par_f:
				break
	
		filtro = json.loads(aux)
		aux1 = filtro["items"][-1]["snippet"]["title"]
		aux2 = filtro["items"][-1]["id"]["videoId"]
		aux3 = 'Nome da música: ' + aux1 + ' Link: www.youtube.com/watch?v=' + aux2
		con.send(aux3.encode())

	aux = ''
	aux1 = ''
	aux2 = ''
	aux3 = ''
	filtro = ''
	http.close()
