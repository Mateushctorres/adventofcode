#P1

#Pegando os dados

with open("./day4/input.txt") as file:
    data = [i for i in file.read().split("\n") ]
    
pares = 0
for section in data:
    primeiro, segundo = section. split(",") #divide na virgula entre os 2
    
    #separa os 2 núMEros dos pares a partir do -
    primeiro = [int(i) for i in primeiro.split("-")]
    segundo = [int(i) for i in segundo.split("-")]
    
    # se um conter inteiramente o outro add 1 a soma
    if primeiro[0] <= segundo[0] and primeiro[1] >= segundo[1]:
        pares += 1
    elif segundo[0] <= primeiro[0] and segundo[1] >= primeiro[1]:
        pares += 1
        
print("Pt1: ", pares)

#P2

pares = 0
for section in data:
    primeiro, segundo = section. split(",") #""
    
    #""
    primeiro = [int(i) for i in primeiro.split("-")]
    segundo = [int(i) for i in segundo.split("-")]
    
    # if primeiro[0] in range(segundo[0], segundo[1]+1) 
    # or primeiro[1] in range(segundo[0], segundo[1]+1):
    #     pares += 1
    # elif segundo[0] in range(primeiro[0], primeiro[1]+1) or segundo[1] in range(primeiro[0], primeiro[1]+1):
    #     pares += 1
    
    if ( primeiro[0] in range(segundo[0], segundo[1]+1) 
        or primeiro[1] in range(segundo[0], segundo[1]+1) 
        or segundo[0] in range(primeiro[0], primeiro[1]+1) 
        or segundo[1] in range(primeiro[0], primeiro[1]+1) ):
        
        pares += 1

print ("Pt2: ", pares)