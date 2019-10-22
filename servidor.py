import socket, _thread, servidor_http

HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 8055             # Porta que o Servidor esta


def Conectado(con, cliente):
    print ('Conectado com', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print ('Requisição do cliente', cliente ,msg.decode())
        
        if(msg.decode() == "\\autores"):
            resp = 'Autores: Marcelo Lima e Robson Vasquez'
            con.send(resp.encode())            
            print('Resposta enviada...')

        else:
            servidor_http.Servidor_HTTP(msg.decode(), con)
            print('Resposta enviada...')                  


    print ('Finalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(Conectado, tuple([con, cliente]))


