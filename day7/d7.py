#Pegando os dados
with open("./day7/input.txt") as file:
    comandos = [comando for comando in file.read().split("\n")]
    
caminho = "/home"
diretorios = {"/home":0}
    
#Tratabdo os comandos em geral
for comando in comandos:
    
    #Comandos que começam com $
    if comando[0] == "$":
        
        # Não fazer nada com o Ls
        if comando[2:4] == "ls": 
            pass
       
        # Cd
        elif comando[2:4] == "cd": 
            
            # voltar para home
            if comando[5:6] == "/": 
                caminho = "/home"
        
            # voltar um dir
            elif comando[5:7] == "..":
                caminho = caminho[:caminho.rfind("/")] # :caminho lẽ do começo até o fim, rfind acha o último / utilizado e retorna p ele

            # Mudança de caminho
            else:
                nome_dir = comando[5:] #Pegando o nome do diretŕoio
                caminho = caminho + "/" + nome_dir # Add ao caminho
                diretorios.update({caminho:0}) # add e dar um update nos caminhos, 0 pq ainda n sabemos o tamanho
      
    # Comandos que não tem $          
    # Não fazer nada com dir
    elif comando[0:3] == "dir":
            pass
        
    # Pegar os tamanahos e ir adicionando
    
    else: 
        tamanho = int(comando[:comando.find(" ")]) #Pegando o tamanho
        
        diretorio = caminho
        for i in range(caminho.count("/")): # Vê quantas / para dentro estamos
            diretorios[diretorio] += tamanho  # adiciona o tamanho ao diretório
            diretorio = diretorio[:diretorio.rfind("/")] # vai adicionando o tamanho de / anterior em / anterior até o home
            
# ----------------  Parte 1  ------------------

total = 0

for diretorio in diretorios:
    if diretorios[diretorio] <= 100000:
        total += diretorios[diretorio]
        
print("Pt1: ", total)