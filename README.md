>>> ChatBot de busca de músicas <<<

Foi desenvolvido um sistema de ChatBot para que um determinado usuário possa consultar informações 
sobre músicas do site YouTube (por exemplo, título, cantor, ano). O usuário enviará uma requisição
para o servidor. Este servidor verificará a requisição e decidirá respondendo ou encaminhando a 
requisição para o servidor HTTP.

>>> Modo de usar <<<

O código possui 2 instâncias:

-> Servidor - Instância que executará o servidor - python3 servidor.py

-> Cliente - Instância que executarão clientes que comunicam com o servidor - python3 main.py

>>> Comandos <<<
• Nível básico: \autores = retorna o valor de uma variável constante com o nome dos integrantes do grupo que o desenvolveu.

• Nível intermediário: \trendmusic = consulta o trending topics do YouTube e retorna o nome da primeira da lista (mais popular) e o link para o Cliente.

• Nível avançado: \music < parâmetro > = consulta a url da música e retorna para o Cliente o link.
