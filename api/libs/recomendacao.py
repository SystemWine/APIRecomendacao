from math import sqrt
from api.models import model_usuario_nota_vinho as votos

def euclidiana(usuario1, usuario2):
    si = {}
    avaliacoes = votos.UsuarioNotaVinhoModel.avaliacoes() 
    for item in avaliacoes[usuario1]:
       if item in avaliacoes[usuario2]: si[item] = 1

    if len(si) == 0: return 0

    soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
                for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])
    return 1/(1 + sqrt(soma))


def getSimilares(usuario):
    avaliacoes = votos.UsuarioNotaVinhoModel.avaliacoes() 
    similaridade = [(euclidiana(usuario, outro), outro)
                    for outro in avaliacoes if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]
   
def getRecomendacoesUsuario(usuario):
    totais={}
    avaliacoes = votos.UsuarioNotaVinhoModel.avaliacoes() 
    somaSimilaridade={}
    for outro in avaliacoes:
        if outro == usuario: continue
        similaridade = euclidiana(usuario, outro)

        if similaridade <= 0: continue

        for item in avaliacoes[outro]:
            if item not in avaliacoes[usuario]:
                totais.setdefault(item, 0)
                totais[item] += avaliacoes[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings=[(total / somaSimilaridade[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings