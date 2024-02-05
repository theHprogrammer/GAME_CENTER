# Bibliotecas
import random

def jogar():
    print('\n\n')
    print('*'*50)
    print('Bem vindo ao jogo de Adivinhação!')
    print('*'*50, end='\n\n')

    total_tentativa = 0
    pontos = 1000
    numero_secreto = random.randrange(1, 101)

    print('Níveis de dificuldade:')
    print('''
            1 - Fácil
            2 - Médio
            3 - Difícil
            ''', end='\n\n')

    nivel = int(input('Escolha o nível de dificuldade: '))

    if (nivel == 1):
        total_tentativa = 20
    elif (nivel == 2):
        total_tentativa = 10
    else:
        total_tentativa = 5


    for rodada in range(1, total_tentativa + 1):
        print(f'Tentativa {rodada} de {total_tentativa}.')

        chute = int(input('Digite um número entre 1 e 100: '))
        print('Voce digitou: ', chute, end='\n\n')
        
        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100 para jogar!', end='\n\n')
            continue

        # Verificações
        acertou = numero_secreto == chute
        maior = numero_secreto > chute
        menor = numero_secreto < chute

        if (acertou):
            print(f'Você acertou e fez {pontos} pontos.', end='\n\n')
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
            if (maior):
                print('Você errou! O número secreto é maior que o chute.', end='\n\n')
                if (rodada == total_tentativa):
                    print(f'O número secreto era {numero_secreto}! Você fez {pontos} pontos.', end='\n\n')
                
            elif (menor):
                print('Você errou! O número secreto é menor que o chute.', end='\n\n')
                if (rodada == total_tentativa):
                    print(f'O número secreto era {numero_secreto}! Você fez {pontos} pontos.', end='\n\n')


    print('Fim do jogo!')
    
if (__name__ == '__main__'):
    jogar()
