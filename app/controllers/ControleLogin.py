from flask import session
from flask_login import login_user, current_user, logout_user
from ..models.entity.Usuario import Usuario
from ..models.dao.LoginDao import LoginDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao

"""
Classe Controller para o Login do sistema
@author - Fabio
@version - 1.0
@since - 23/05/2023
"""

class ControleLogin:
    
    def login(self, user: str, pssd: str) -> int:
        #########################################################################################
        # Essa função recebe o usuário e a senha para autenticação no sistema.
        
        # PARAMETROS:
        #   user = Usuário informado no form de login;
        #   pssd = Senha informada no form de login.
        
        # RETORNOS:
        #   return 1 = Retorna 1 se o usuário existe e está correto e usuário Administrador;
        #   return 2 = Retorna 2 se o usuário existe e está correto e usuário Tec. Segurança;
        #   return 3 = Retorna 3 se o usuário existe e está correto e usuário Vigilante;
        #   return 4 = Retorna 4 se a senha/usuário estão incorretos;
        #   return 5 = Retorna 5 se o usuário está inativo ou deletado;
        #   return 6 = Retorna 6 se o usuário não existe;
        #########################################################################################
        
        usuario = Usuario()
        usuario.set_usuario(user)
        usuario.set_senha(pssd)
        if user == "ADMIN":
            return self.loginAdm(usuario)
        else:
            loginDao = LoginDao()
            userResp = loginDao.consultaUsuario(usuario)
            if userResp != 0:
                if usuario.get_delete() != True and usuario.get_ativo() != True: #Verifica se o usuário está inativo ou deletado
                    if usuario.verificarSenha(): #Verfica a senha digitada
                        self.verficaTrocaSenha(usuario) #Verifica se usuário que está logando solicitou troca de senha
                        login_user(userResp)
                        session["nome"] = usuario.get_nome()
                        session["usuario"] = usuario.get_usuario()
                        if usuario.get_grupo() == "ADM":
                            return 1
                        elif usuario.get_grupo() == "TEC":
                            return 2
                        elif usuario.get_grupo() == "VIG":
                            return 3
                    else:
                        return 4
                else:
                    return 5
            else:
                return 6
    

    def loginAdm(self, usuario: Usuario) -> int:
        #########################################################################################
        # Essa função recebe o usuário ADMIN e vefica o usuário e senha digitado, mas se não existir
        # ele é adicionado no banco.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com usuário e senha.
        
        # RETORNOS:
        #   return 1 = Retorna 1 se o usuário existe e está correto e usuário Administrador;
        #   return 4 = Retorna 4 se a senha/usuário estão incorretos.
        #########################################################################################

        loginDao = LoginDao()
        userResp = loginDao.consultaUsuario(usuario) #Verifica se o ADMIN já existe
        if userResp != 0:
            if usuario.verificarSenha():
                self.verficaTrocaSenha(usuario) #Verifica se usuário que está logando solicitou troca de senha 
                login_user(userResp)
                session["nome"] = usuario.get_nome()
                session["usuario"] = usuario.get_usuario()
                return 1
            else:
                return 4
        else:
            controleManterUsuario = ManterUsuarioDao()
            controleManterUsuario.adicionaAdm(usuario)
            controleManterUsuario.inserirUsuario(usuario)
            userResp = loginDao.consultaUsuario(usuario)
            if usuario.verificarSenha():
                self.verficaTrocaSenha(usuario) #Verifica se usuário que está logando solicitou troca de senha
                login_user(userResp)
                session["nome"] = usuario.get_nome()
                session["usuario"] = usuario.get_usuario()
                return 1
            else: 
                return 4


    def verficaTrocaSenha(self, usuario: Usuario) -> None:
        #########################################################################################
        # Essa Função recebe o usuário que está efetuando o login no sistema, e verifica se foi
        # solicitado a troca de senha, caso tenha solicitado o sistema retira a solicitação.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com usuário e senha.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        loginDao = LoginDao()
        if loginDao.verficaTrocaSenha(usuario):
            loginDao.atulizaTrocaSenha(usuario)
        else:
            pass


    def logout(self) -> None:
        #########################################################################################
        # Essa Função que efetua o logout do usuário no sistema.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   Não tem retornos.
        #########################################################################################
        
        logout_user()
        session.clear()