#Apenas 4 locais onde pode empilhar os containers e seu equipamento permite empilhar no máximo 3 containers.
#Um novo container deve ser colocado no local com a pilha mais baixa disponível (se mais de um local tiver a mesma quantidade de
#containers, tanto faz em que pilha será adicionado).

#Adicionado a partir de um código informado e o sistema não pode permitir códigos repetidos.
#Remoção também é preciso informar o código do container, mas o mesmo somente será removido se estiver no topo da pilha.

pilha_a = [] 
pilha_b = [] 
pilha_c = [] 
pilha_d = []

list_pilha_total = []

def pilha_total():
    
    for i in pilha_a:
        list_pilha_total.append(pilha_a[i])

    for i in pilha_b: 
        list_pilha_total.append(pilha_b[i])

    for i in pilha_c: 
        list_pilha_total.append(pilha_c[i]) 

    for i in pilha_d: 
        list_pilha_total.append(pilha_d[i])  

    return list_pilha_total

def menor_pilha():
    menor_pilha = pilha_a
    if len(pilha_b) < len(pilha_c):
        menor_pilha = pilha_b
    if len(pilha_c) < len(pilha_d):
        menor_pilha = pilha_c
    else:
        menor_pilha = pilha_d

    return menor_pilha

def espaco_cheio():
    if len(pilha_a) == 3 and len(pilha_b) == 3 and len(pilha_c) == 3 and len(pilha_d) == 3:
        print("Impossível empilhar! Todos os espaços possuem contâiner.")

def adicionar_container(codigo):
    for container in list_pilha_total:
        if codigo == list_pilha_total[container]:
            print("Código inválido! Contâiner já adicionado")
    return

pilha_a.append(1)
adicionar_container(1)