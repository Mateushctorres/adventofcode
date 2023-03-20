with open("./day6/input.txt") as file:
    input = file.read()
    

#Pt1

for num in range(4, len(input)+1): #4 pq começa do último de uma sequência de 4 // len(input) + 1 pois começa de 0 e queremos ir até o fim
    list = set(input[(num-4):num]) #num(4)-4 = começo, até o num = fim
    # set para printar apenas os num únicos de cada
    if len(list) == 4:
        print ("Pt1: ", num)
        break
    
#Pt2


for num in range(14, len(input)+1): 
    list = set(input[(num-14):num]) 
    if len(list) == 14:
        print ("Pt2: ", num)
        break
    