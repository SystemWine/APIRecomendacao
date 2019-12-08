from flask_restful import Resource, reqparse
from api.models.model_usuario_nota_vinho import UsuarioNotaVinhoModel
from api.libs.recomendacao import *

parser = reqparse.RequestParser()
parser.add_argument('id_usuario')
#https://flask-restful.readthedocs.io/en/latest/reqparse.html

class Teste(Resource):
    def get(self):
        return getSimilares('thales.areis@gmail.com')

class ObterRecomendacoesUsuario(Resource):
    def get(self):
        data = parser.parse_args()
        print('****************************')
        print(data)
        print('****************************')
        id_usuario = data['id_usuario']

        print('_______****************************')
        print(UsuarioNotaVinhoModel.avaliacoes())
        print('_______****************************')

        def to_json(x):
            return {
                '{}'.format(x.IdUsuario): x.Nota,
            }

        avaliacoes = UsuarioNotaVinhoModel.avaliacoes()


        print('xxx_______****************************')
        print(avaliacoes)
        print('xxx_______****************************')
        
            
        return UsuarioNotaVinhoModel.avaliacoes()
        # return {'notas': list(map(lambda x: to_json(x), UsuarioNotaVinhoModel.notas_por_usuario(id_usuario)))}