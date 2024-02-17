import socket

# Configurar o cliente
cliente = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
endereco_servidor = ('2804:25ac:40e:8b00:a13b:e094:9f58:820b', 12345)

# Conectar ao servidor
cliente.connect(endereco_servidor)

# Enviar uma mensagem ao servidor
mensagem_cliente = 'Olá, servidor!'
cliente.send(mensagem_cliente.encode())

# Receber mensagem do servidor
mensagem_servidor = cliente.recv(1024)
print(f'Mensagem do servidor: {mensagem_servidor.decode()}')