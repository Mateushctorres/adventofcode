#Implementação de uma pilha em Python

def push(stack, item):
    #Adiciona um item ao topo da pilha (1a1)
    return stack.append(item)

def pop(stack):
    #Retorna e remove o item do topo da pilha (1a1)
    if not stack:
        raise ValueError("Pilha vazia")
    #return stack.pop(0)
    return stack.pop() # ou pop(-1)

def peek(stack):
    #Consulta o item do topo
    return stack[len(stack) - 1]

def inicializa(stack, valores):
    for c in valores:
        push( stack, int(c) )

def movethree( origem, destino, qtde):
    temp = []
    for i in range(qtde):
        val = pop(origem)
        push(temp, val)
    for i in range(qtde):
        val = pop(temp)
        push(destino, val)
        
pilha1 = ["Q","W","P","S","Z","R","H","D"]
pilha2 = ["V","B","R","W","Q","H","F"]
pilha3 = ["C","V","S","H"]
pilha4 = ["H","F","G"]
pilha5 = ["P","G","J","B","Z"]
pilha6 = ["Q","T","J","H","W","F","L"]
pilha7 = ["Z","T","W","D","L","V","J","N"]
pilha8 = ["D","T","Z","C","J","G","H","F"]
pilha9 = ["W","P","V","M","B","H"]

pilhas =  [pilha1, pilha2, pilha3, pilha4, pilha5, pilha6, pilha7, pilha8, pilha9]


#pegando os dados
with open("./day5/input.txt") as file:
    instrucoes = [i for i in file.read().split("\n")]
    
for instrucao in instrucoes:
    instrucao = instrucao.replace("move", "").replace("from", "").replace("to", "").strip().split() #deixar apenas os números
    qtde = int(instrucao[0])
    origem = int(instrucao[1])-1 #-1 pq começa do 0
    destino = int(instrucao[2])-1
    instrucao = movethree(pilhas[origem], pilhas[destino], qtde)


#   ---   RESPOSTA PARTE 2   ---   #
for p in pilhas:
    print("Pt2: ",p[-1])
    

