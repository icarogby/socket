import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endereco_servidor = ('localhost', 12345)
servidor.bind(endereco_servidor)
servidor.listen(1)

print('Aguardando conexão...')

# Aceitar a conexão do cliente
while True:
    conexao, endereco_cliente = servidor.accept()
    print(f'Conectado com {endereco_cliente}')

    while True:
        # Receber dados do cliente
        dados = conexao.recv(1024)
        print(f'Mensagem do cliente: {dados.decode()}')

        # Enviar uma mensagem ao cliente
        mensagem_servidor = 'Olá, cliente!'
        conexao.send(mensagem_servidor.encode())

