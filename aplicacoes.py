import time

#Encontrar o maior valor na lista - Exemplo1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0] #recebeu o numero 17

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]
print("O Maior número da lista é:", maior_numero)

#Exemplo2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2:", maior)

#Exemplo3
ultima_lista = my_list[:]
mel = ultimma_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
        mel = i
print("Mior valor 3:", mel)

#Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamao", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Elemento encontrado no índice:", i)
else: 
    print("NÃO ENCONTRADO!!!")

#Conferidor de aposta em loteria
sorteados = [5, ,11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
    if numero in apostados:
        



time.sleep(3)