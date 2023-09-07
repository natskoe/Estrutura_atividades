#Implemente um programa principal que utilize a pilha através de
#chamada de funções: empilhar, desempilhar, limpar, mostrar pilha,
#acessar o topo da pilha, sair do programa informando “Sair”

# append --> Acrescenta no topo
# pop() --> Remove do topo | pop(indice) 
# top --> Acessa o elemento do topo (Pilha[-1])
# len(pilha) == 0 --> Pilha vazia
# clear --> Limpa a pilha

# Base nunca desloca, sempre [0], o topo é mutável.


pilha = []
    

def empilhar(elemento_pilha):
    pilha.append(elemento_pilha)

def desempilhar():
    if len(pilha)==0:
        print("Não há o que desempilhar.")
    else:
        pilha.pop()

def limpar():
    pilha.clear()

def mostrar_pilha():
    print(pilha)

def mostrar_topo_pilha():
    if len(pilha)==0:
        print("Não há elemento na pilha, não há topo.")
    else:
        print(pilha[-1])

sair = False
while sair == False:
    print('Para sair, digite \'sair\'.')
    acao = input('O que você deseja fazer?\n1. Empilhar na pilha.\n2. Desempilhar da pilha.\n3. Limpar a pilha.\n4. Mostrar o topo da pilha.\n5. Mostrar a pilha.\n->')
    if acao.lower() == 'sair':
        sair = True 
    else:
        acao = int(acao) 
        if acao == 1:
            a = str(input('Qual o elemento a ser colocado na pilha?'))
            empilhar(a)
        elif acao == 2:
            desempilhar()
        elif acao == 3:
            limpar()
        elif acao == 4:
            mostrar_topo_pilha()
        elif acao == 5:
            mostrar_pilha()