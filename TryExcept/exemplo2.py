try:
    numero1 = 10
    numero2 = 2
    resultado = numero1 / numero2
    print(f'o resultado é {resultado}')
except ZeroDivisionError:
    print('Segundo numero não pode ser zero')
else:
    print('Divisão Realizada com Sucesso')
finally:
    print('Fim da Divisão')

