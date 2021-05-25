#!/usr/bin/python
# -*- encode: utf-8 -*-
# autor: alison silva

# importa tudo do modulo random
from random import *

# variavel que conta as tentativas do jogador.
tentativas = 0

class Cores:
    """
    classe para armazenar as cores que serao
    utilizadas para estilizar o jogo.
    """
    verde = "\033[5;32m"
    amarelo = "\033[5;33m"
    vermelho = "\033[5;31m"

def titulo():
    print("\n%s"%(Cores.amarelo+" JOGO DE ADVINHACAO ".center(30, "-")))
    print("\033[0msera gerado um numero aleatorio entre (1-100)")
    print("tente acerta-lo")    

def numero_gerado():
    """
    funcao que gera um numero aleatorio
    entre 1 e 100.
    """
    ng = choice(range(1, 101))
    return ng

def palpite():
    """
    funcao que pede para o usuario palpitar
    um numero
    """
    while True:
        numero = int(input("\033[0\nmseu palpite: "))
        if numero > 0 and numero < 101:
            return numero
        else:
            print(Cores.vermelho+"palpite deve estar entre 1 e 100\033[0m")

def verifica_numero(ng, numero, tentativas):
    """
    funcao que verifica se o numero palpitado
    pelo usuario é o mesmo que foi gerado
    aleatoriamente
    """
    tentativas += 1
    if numero == ng:
        # se for igual
        print("\033[0mvoce acertou o numero "+Cores.amarelo+"%d !!"%(ng))
        print(f"tentativas {tentativas}")

    else:
        # se nao for igual
        if numero > ng:
            # se for maior que o sorteado
            print("\033[0mpalpite um numero "+Cores.vermelho+"MENOR")
            numero = palpite()
            verifica_numero(ng, numero, tentativas)

        elif numero < ng:
            # se for menor que o sorteado
            print("\033[0mpalpite um numero "+Cores.verde+"MAIOR")
            numero = palpite()
            verifica_numero(ng, numero, tentativas)

def main():
    """
    funcao principal do jogo.
    """
    while True:
        titulo()
        try:
            numero = palpite()
            ng = numero_gerado()
            global tentativas
            verifica_numero(ng, numero, tentativas)
            opcao = input("\033[0mjogar novamente (s/n)")
            if opcao.upper() == 'S':
                continue

            elif opcao.upper() == 'N':
                print("saindoo...")
                break

        except KeyboardInterrupt:
            print("saindoo...")
            break

if __name__ == "__main__":
    main()