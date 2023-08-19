from votes import Votes

# Input data
# candidatos
while True:
    try:
        n_cand = int(input('Quantos candidatos são? (Máximo de 9) '))
        if n_cand <= 9:
            break
        else:
            print('Número inválido, tente novamente.')
    except:
        print('Número inválido, tente novamente.')
name_cand = []
for i in range(n_cand):
    name = str(input(F'Digite o nome do candidato {i + 1}: ')).capitalize()
    name_cand.append(name)

# eleitores
while True:
    try:
        n_elei = int(input('Quantos eleitores são? (Máximo de 9) '))
        if n_elei <= 9:
            break
        else:
             print('Número inválido, tente novamente.')
    except:
        print('Número inválido, tente novamente.')

# votos
votos = {}
for i in range(n_elei):
    lista = []
    print(30 * '=')
    for b in range(n_cand):
        vote = str(input(f'Voto {b + 1}: ')).capitalize()
        lista.append(vote)
    votos[i + 1] = lista

# processing
Votes.analise(votos, name_cand)