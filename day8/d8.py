
with open("./day8/input.txt") as file:
    data = [linha.strip() for linha in file.readlines
    ()]

LINHAS = len(data)            # num de linhas
COLUNAS = len(data[0])      # num of colunas

bordas = (LINHAS*2) + ((COLUNAS-2)*2)      # todas as árvores nas bordas são visíveis
total = bordas                           # add as de borda ao total de visíveis
scores = []                             # total de centro

# Iterar pelas árvores que não estão nas bordas
for linha in range(1, LINHAS-1): 
    for col in range(1, COLUNAS-1):
        arvore = data[linha][col]           # árvore procurada

        # Pegar todas as arvores horizontais e verticais
        esquerda = [data[linha][col-i] for i in range(1, col+1)]
        direita = [data[linha][col+i] for i in range(1, COLUNAS-col)]
        cima = [data[linha-i][col] for i in range(1, linha+1)]
        baixo = [data[linha+i][col] for i in range(1, LINHAS-linha)]

        # === PARTE 1 ===
        # Checar se a árvore mais alta de todos os lados bloqueia a vista da árvore
        if max(esquerda)<arvore or max(direita)<arvore or max(cima)<arvore or max(baixo)<arvore:
            total += 1

        # === PARTE 2 ===
        
        # Achando o Score
        score = 1
        for lst in (esquerda, direita, cima, baixo):
            track = 0
            for i in range(len(lst)):
                if lst[i] < arvore:
                    track += 1
                elif lst[i] >= arvore:
                    track += 1
                    break
            
            score *= track

        scores.append(score)

print("Pt1: ", total)
print("Pt2: ", max(scores))