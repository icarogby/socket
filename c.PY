import socket

# Configurar o cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endereco_servidor = ('127.0.0.1', 12345)

# Conectar ao servidor
cliente.connect(endereco_servidor)

# Enviar uma mensagem ao servidor
mensagem_cliente = 'Olá, servidor!'
cliente.send(mensagem_cliente.encode())

# Receber mensagem do servidor
mensagem_servidor = cliente.recv(1024)
print(f'Mensagem do servidor: {mensagem_servidor.decode()}')