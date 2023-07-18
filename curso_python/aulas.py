'''
#Isso é um comentário

#funcionamento do print()
print(12, 34)
print(56, 78, sep="-")
print(910, 1112, sep="-", end="\r\n")

#TIPOS----------------------------------------------------------------------------

#string -> texto
"""
Docstring
Isso não é um comentário, mas não executa nada
"""
#aspas simples
print('Lucas Zappani')
#aspas duplas
print("Lucas")
#Escape
print("Lucas \"Zappani\"")

#r
print(r"Lucas \"Zappani\"")
#melhor opção que r ou escape
print('Lucas "Zappani"')
print("Lucas 'Zappani'")

#números
#int
print(10)
print(-10)
print(0)
#float
print(1.0, 1.1)
#boolean
print(True, 1)
print(False, 0)

#Para saber o tipo de dado é necessario usar type()
print(type("Lucas Zappani"), type(-1), type(-1.0))

#Conversão de tipo -------------------------------------------------------------------
print(str(11), int(1.0))
print(type(str(11)), type(int(1.0)))


#Variáveis ---------------------------------------------------------------------------
nome_completo = 'Lucas Zappani'
soma_de_numeros = 1 + 2 + 3
print(nome_completo, soma_de_numeros) 
print(type(nome_completo), type(soma_de_numeros) )

nome = 'Lucas'
idade = 21
maior_de_idade = idade >= 18

print("Nome:", nome, "Idade:", idade)
print("É maior de idade?:", maior_de_idade)

#Aula 24 - Exercicío 1--------------------------------------------------------

nome = 'Lucas' 
sobrenome = 'Zappani Siqueira'
idade = 21
ano_atual = 2023
ano_nascimento = ano_atual - idade
maior_de_idade = idade >= 18
altura_metros = 1.83

print("Nome:", nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano do nascimento:', ano_nascimento)
print('É maior de idade ?', maior_de_idade)
print('Altura em metros:', altura_metros, 'm')

#Operadores aritméticos ---------------------------------------------------

adicao = 10 + 10 
subtracao = 10 - 5
multiplicacao = 10 * 10
divisao = 10 / 2.2
divisao_inteira = 10 // 2.2
exponenciacao = 10 ** 3
resto_da_divisao = 55 % 2

print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(exponenciacao)
print(resto_da_divisao)


#Aula 29 - Exercicío 2--------------------------------------------------------

nome = 'Lucas Zappani Siqueira'
altura = 1.83
peso = 76.0
imc = peso / (altura*altura)

print(f'{nome} tem {altura} m de altura,\npesa {peso} kg\ne seu IMC é {imc:.2f}.')

#Aula 32 - formatação -------------------------------------------------------------------------------------------------------

a = 'A'
b = 'B'
c = 1.1 
string = "a={nome0} b={nome1} c={nome2:.2f}"
formato = string.format(
    nome0=a, nome1=b, nome2=c
    )
print(formato)

#Aula 33 - função input-------------------------------------------------------------------------------------------------------

#nome = input('Qual o seu nome? \n')
#print(f"O seu nome é {nome =}.")

numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos numeros é: {int_numero_1 + int_numero_2}')
'''

#Aula 38 - Exercicio 3-------------------------------------------------------------------------------------------------------

valor1 = input('Digite um valor:')
valor2 = input('Digite outro valor:')

intvalor1 = int(valor1)
intvalor2 = int(valor2)

if intvalor1 > intvalor2:
    print(f'{intvalor1 =} é maior que o {intvalor2 =}.')

elif intvalor2 > intvalor1:
    print(f'{intvalor2 =} é maior que o {intvalor1 =}.')

else:
    print('Os valores são iguais!')

#Aula 39 -------------------------------------------------------------------------------------------------------















