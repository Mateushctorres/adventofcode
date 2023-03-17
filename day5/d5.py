#Implementação de uma pilha em Python

def push(stack, item):
    #Adiciona um item ao topo da pilha e retorna uma nova pilha
    #return stack.insert(0, item)
    return stack.append(item)

def pop(stack):
    #Remove e retorna o item no topo da pilha e uma nova pilha
    if not stack:
        raise ValueError("Pilha vazia")
    #return stack.pop(0)
    return stack.pop() # ou pop(-1)

def peek( stack):
    #Consulta o último sem retirar
    return stack[ len(stack) - 1]

def inicializa(stack, valores):
    for c in valores:
        push( stack, int(c) )
        
#Para realizar as operações descritas no input
def move( origem, destino, qtde):
    for i in range(qtde):
        val = pop(origem)
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
    origem = int(instrucao[1])-1
    destino = int(instrucao[2])-1
    instrucao = move(pilhas[origem], pilhas[destino], qtde)

for p in pilhas:
    print(p)