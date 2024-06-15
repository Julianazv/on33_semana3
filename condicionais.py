#idade = 34
#if idade >= 18:
#    print ('se você é maior de idade')

idade = 34
if idade >= 18:
    print ('acesso liberado')
else:
    print ('acesso negado!')

temperatura = 26
if temperatura > 25:
    print ('frio')
else:
    print ('quente')

nota = 8
if nota >= 7:
    print('Você foi aprovada!')
elif nota == 5:
    print('Você está de Recuperação')
else:
    print('Você está Reprovado')

nota = float(input('insira a nota da aluna (de 0 a 10)'))
if (nota >= 7):
    print ('Muito bem!! Aprovada!!!')
else:
    print ('poxa, não foi dessa vez')