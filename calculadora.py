from time import sleep
import sys

print("Calculadora de terminal \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")
numeros = int(input("Escolha um número \n ~>"))

# Opções disponíveis

if numeros == 1:
    print('Você escolheu (Soma) \n', '=-' * 10)
    resultado = ('Soma')

elif numeros == 2:
    print('Você escolheu (Subtração) \n', '=-' * 10)
    resultado = ('Subtração')

elif numeros == 3:
    print('Você escolheu (Multiplicação \n)', '=-' * 10)
    resultado = ('Multiplicação')


elif numeros == 4:
    print('Você escolheu (Divisão) \n', '=-' * 10)
    resultado = ('Divisão')

else:
    print('Otário vai achando que vai bugar meu código')
    sys.exit('Tenta de novo rsrsrs')

# Resultado
p3 = []
p1 = int(input("Escreve seu primeiro número (de acordo com a sua escolha anterior)\n~>"))
p2 = int(input("Escreve agora seu segundo número\n~>"))
print("=-" * 10)

def soma(p3):
    p3 = p1 + p2
    return p3
def Subtracao(p3):
    p3 = p1 - p2
    return p3 
def Multiplicacao(p3):
    p3 = p1 * p2 
    return p3
def Divisao(p3):
    p3 = p1 / p2
    return p3

if resultado == 'Soma':
    print('O resultado é', soma(p3))
elif resultado == 'Subtração':
    print('O resultado é', Subtracao(p3))
elif resultado == 'Multiplicação':
    print('O resultado é', Multiplicacao(p3))
elif resultado == 'Divisão':
    print('O resultado é', Divisao(p3))
else:
    print('Resultado invalído')

    
