from ..Tables import SysUser
from ..entity.Usuario import Usuario
from ...extensions.Database import DB
import json
import sys

#Classe para trabalhar com o banco de dados
class LoginDao:
    
    def consultaUsuario(self, login: Usuario):
        #########################################################################################
        # Função que verifica se o usuário que está acessando o sistema existe no banco de dados.
         
        # PARAMETROS:
        #   login = Classe Usuario que contem o usuário e a senha.
        
        # RETORNO:
        #   return user = Retorna o usuário que achou no banco.
        #########################################################################################

        # dic = {
        #     'teste': 15,
        #     'teste2': 0,
        # }
        # json_data = json.dumps(dic)

        try:
            user = SysUser.query.filter_by(us_usuario=login.get_usuario()).first()
            if user:
                login.set_id(user.id)
                login.set_email(user.us_email)
                login.set_grupo(user.us_grupo)
                login.set_complex(user.us_complex)
                login.set_ativo(user.us_ativo)
                login.set_delete(user.us_delete)
                login.set_senhaCompara(user.us_senha)
                return user
            else:
                return 0 
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            pass
        # user.teste = bytes(json_data, encoding='utf-8')
        # DB.session.commit()
        # print(user.teste)
        # json_data = user.teste.decode("utf-8")
        # print(json_data)
        # data = json.loads(json_data)
        # print(data['teste'])
        
         