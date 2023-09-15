import random

class MediaAluno:
    medias_alunos = [['Bob Esponja', None, None, None, None],
                    ['Patrick Estrela', None, None, None, None],
                    ['Sandy Bochechas', None, None, None, None],
                    ['Lula Molusco Tentáculos',None, None, None, None],
                    ['Gary Caracol', None, None, None, None]]

    print('Essas são as medias salvas dos alunos: ')
    for aluno in medias_alunos:
        for i in range(1, len(aluno)):
            #Percorre a matriz, tirando o nome pra pegar as notas.
            aluno[i] = random.randint(0, 10)

        nome = aluno[0]
        notas = aluno[1:]

        soma_nota = 0
        for nota in notas:
            soma_nota += nota
        a = len(aluno)-1
        media_nota = soma_nota/a
        
            
        if media_nota >= 6:
            print(f'{nome} aprovado com média {media_nota:.2f}')    
        else:
            print(f'{nome} reprovado com média {media_nota:.2f}')   


