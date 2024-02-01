#!/usr/bin/env python3
"""
client.py - Script para conexão em um servidor de sockets TCP.
"""
__version__ = "0.1.0"
__author__ = "Alex Soares"
__license__ = "Unlicense"

import socket 

def client():
    # Criação do socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        # Conecta-se ao servidor utilizando o endereço IP e porta fornecidos
        client_socket.connect(("localhost", 9473)) 
        while True:
            # Solicita que o usuário insira uma mensagem
            msg = input("Digite uma mensagem aqui: ")

            # Envia a mensagem codificada para o servidor
            client_socket.send(msg.encode())
    except KeyboardInterrupt:
        print("\nConexão encerrada")

if __name__ == "__main__":
    # Inicia o cliente quando o script é executado
    client()