#!/usr/bin/env python3
"""
server.py - Script para criar um servidor de sockets TCP.
"""
__version__ = "0.1.0"
__author__ = "Alex Soares"
__license__ = "Unlicense"

import socket
import sys

def server():

    # Tamanho máximo dos dados que podem ser recebidos de uma vez
    data_payload = 1024 

    # Criação do socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associação do socket ao endereço local e à porta
    server_socket.bind(("localhost", 9473))

    # Aguarda conexões
    server_socket.listen()

    try:
        # Aceita a conexão quando um cliente se conecta
        connection, address = server_socket.accept()
    except KeyboardInterrupt:
        print("\nExecução encerrada")
        sys.exit(1)

    while True:
        # Recebe os dados do cliente
        data = connection.recv(data_payload) 
        if not data:
            break
        # Exibe a mensagem recebida e o endereço do cliente
        print(f"Nova mensagem do host {address}: {data.decode()}")

    #Encerra a conexão
    connection.close() #Encerra a conexão
 

if __name__ == "__main__":
    server()