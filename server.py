#!/usr/bin/env python3

import socket #importa a lib de sockets

def server():

    data_payload = 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando o socket, AF_INET se refere a familia do socket e o SOCK_STREAM ao tipo, nesse caso tipo tcp

    server_socket.bind(("localhost", 9473)) #com o metodo bind informamos o IP e porta onde o socket é criado

    server_socket.listen() #Faz com que o o socket aguarde uma conexão

    connection, address = server_socket.accept() #Mostra quem esta se conectando

    while True:
        data = connection.recv(data_payload) #O metodo recv recebe os dados e tem como parametro o tamanho das mensagem
        if not data:
            break
        print(f"Nova mensagem do host {address}: {data.decode()}") #Print o host que esta se conectando e a mensagem
        
    connection.close() #Encerra a conexão
 
server() #Chama a função