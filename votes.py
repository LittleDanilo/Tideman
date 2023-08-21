class Votes:
    def analise(votes, name_cand):

        # criando uma lista de classificação
        classificacao = {}
        for n in name_cand: # para cada nome na lista de candidatos ele da um valor inicial de 0
            classificacao[n] = 0
        
        # conferindo a posição de cada candidato nas listas de votação e dando seus pontos
        for v in votes: # pra cada voto na lista de votos
            voteList = votes[v]
            for vote in voteList:
                for i in range(9):
                    try:
                        if vote == voteList[i]:
                            classificacao[vote] += i
                    except:
                        pass
        
        # print vencedor
        vencedorV = 200
        name = ''
        for c in classificacao:
            valor = classificacao[c]
            if vencedorV > valor:
                vencedorV = valor;
                name = c
        print(30*'=')
        print(F'o vencedor é: {name}')