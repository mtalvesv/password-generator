import random
import os

class Generator:

    def gerar_senha(valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(nova_senha, valores):
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(
                f"\nsite: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}")

        print('Arquivo salvo')