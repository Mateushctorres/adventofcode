#P1

#Pegando os dados

with open("./day4/input.txt") as file:
    data = [i for i in file.read().split("\n") ]
    
print(data)

pares = 0

for section in data:
    primeiro, segundo = section. split(",") #divide na virgula entre os 2
    print(primeiro, segundo)
    
    #separa os 2 núemros dos pares a partir do -
    primeiro = [int(i) for i in primeiro.split("-")]
    segundo = [int(i) for i in segundo.split("-")]
    
    # se um conter inteiramente o outro add 1 a soma
    if primeiro[0] <= segundo[0] and primeiro[1] >= segundo[1]:
        pares += 1
    elif segundo[0] <= primeiro[0] and segundo[1] >= primeiro[1]:
        pares += 1
        
print("Pt1: ", pares)