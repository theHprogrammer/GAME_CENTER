import forca
import adivinhacao

print('*'*50)
print('Central de Jogos!')
print('*'*50, end='\n\n')

def _menu():
    print('''
            === MENU ===
            1 - Adivinhação
            2 - Forca
            0 - Sair
            ''', end='\n\n')

def _comecar_jogo():
    encerrar = False
    
    while (not encerrar):
        _menu()
        jogo = int(input('Escolha o jogo: '))
        
        if (jogo == 1):
            adivinhacao.jogar()
        elif (jogo == 2):
            forca.jogar()
        elif (jogo == 0):
            encerrar = True
        else:
            print('Opção inválida!', end='\n\n')
            continue

if (__name__ == '__main__'):
    _comecar_jogo()
    print('\n\nFim da central de jogos!')