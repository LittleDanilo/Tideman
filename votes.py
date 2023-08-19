
class Votes:

    def analise(votes, name_cand):
        classificacao = {}
        valor = 1000
        vencedor = ''

        for n in name_cand:
            classificacao[n] = 0
        
        for i in votes:
            vote = votes[i]
            for n in range(9):
                try:
                    if name_cand[n] == vote[n]:
                        classificacao[name_cand[n]] += n-1
                except:
                    pass

        for i in classificacao:
            if valor > classificacao[i]:
                valor = classificacao[i]
                vencedor = i
        
        print(30*'=')
        print(f'O vendedor foi: {vencedor}')