from string import ascii_letters #importa todas as letras do alfabeto, maiúsculas e minúsculas

#P1

#Pegando os dados

with open("./day3/input.txt") as file:
    data = [i for i in file.read().split("\n") ]
    
print(data) 

#Dividindo os Rucksacks na metade

soma = 0

for rucksack in data:
    metade = len(rucksack)//2 # 2 barras pq só uma vem um double e quero int
    
    #set divide cada um em suas letras únicas e individuais
    esquerda = set(rucksack[:metade]) #começo até metade
    direita = set(rucksack[metade:]) #metade até final
    
    print(rucksack, esquerda, direita)
    
    for priority, char in enumerate (ascii_letters): #dá um número pra cada letra começando por 0 a
        if char in esquerda and char in direita:
            soma += priority + 1 # +1 pq o enumerate começa do zero mas no ex começa do 1
            
print("Pt1 =", soma)

#P2

f = 3
total = 0

for i in range(0, len(data), 3): # começa no 0 e vai até o final de 3 em 3
    rucksacks = data[i:f]
    f += 3 #vai do i 0 até o f de 3 em 3 zerando cada vez começando de 0-3, 0-6, 0-9
    
    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]: # se tiver a mesma letra pelo código nos 3... 
            total += priority + 1
            
print("Pt2 =", total)