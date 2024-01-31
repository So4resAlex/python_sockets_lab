#!/usr/bin/env python3

import socket #importa a lib de sockets

def client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando o socket, AF_INET se refere a familia do socket e o SOCK_STREAM ao tipo, nesse caso tipo tcp
    client_socket.connect(("localhost", 9473)) #Faz a conexão no ip e porta informados

    while True:
        msg = input("Digite uma mensagem aqui: ")
        client_socket.send(msg.encode())

client()