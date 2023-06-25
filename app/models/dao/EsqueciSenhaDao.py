from ..entity.Usuario import Usuario
from ..Tables import SysUser
from ...configurations.Database import DB
import sys

"""
Classe Dao para funções do esquci a senha
@tables - SysUser
@author - Fabio
@version - 1.0
@since - 13/06/2023
"""

class EsqueciSenhaDao:

    def insereHash(self, usuario: Usuario) -> bool:
        #########################################################################################
        # Essa Função insere a solicitação de troca de senha para o usuário.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com os dados do usuário.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso;
        #   return False = Retorna False caso ocorra erro na inserção.
        #########################################################################################

        sysuser = SysUser.query.get(usuario.id)
        sysuser.us_hashNovaSenha = usuario.hashSenhaNova
        sysuser.us_senhaNova = usuario.senhaNova

        DB.session.commit()
        return True
        


    def verificaUsuario(self, usuario: Usuario):
        #########################################################################################
        # Essa Função verifica se o usuário e e-mail digitado existe no banco.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com usuário e senha.
        
        # RETORNOS:
        #   return usuario = Retrona instancia do usuário com todos os dados;
        #   return 0 = Retrona 0 caso não encontre o usuário.
        #########################################################################################

        sysuser = SysUser.query.filter(SysUser.us_usuario==usuario.usuario, SysUser.us_email==usuario.email, SysUser.us_ativo==False, SysUser.us_delete==False).first()
        if sysuser:
            usuario.id = sysuser.id
            usuario.nome = sysuser.us_nome
            usuario.grupo = sysuser.us_grupo
            usuario.complex = sysuser.us_complex
            usuario.ativo = sysuser.us_ativo
            usuario.delete = sysuser.us_delete
            usuario.senhaCompara = sysuser.us_senha
            usuario.hashSenhaNova = sysuser.us_hashNovaSenha
            usuario.senhaNova = sysuser.us_senhaNova
            return usuario
        else:
            return 0


    def verificaHash(self, hash: str) -> bool:
        #########################################################################################
        # Essa Função verifica se o hash existe.
        
        # PARAMETROS:
        #   hash = Hash que foi passado pela URL do e-mail.
        
        # RETORNOS:
        #   return False = Retrona False caso o hash exista;
        #   return True = Retrona True caso o hash não exista.
        #########################################################################################

        sysuser = SysUser.query.filter(SysUser.us_hashNovaSenha==hash).first()

        if sysuser:
            return False
        else:
            return True
        

    def trocaSenha(self, hash: str, usuario: Usuario) -> bool:
        #########################################################################################
        # Essa Função troca a senha do usuário que solicitou.
        
        # PARAMETROS:
        #   hash = Hash que foi passado pela URL do e-mail;
        #   usuario = Instancia da classe Usuario com a nova senha;
        
        # RETORNOS:
        #   return False = Retorna True caso foi alterado com sucesso;
        #   return True = Retorna False caso ocorra erro na alteração.
        #########################################################################################

        sysuser = SysUser.query.filter(SysUser.us_hashNovaSenha==hash).first()

        sysuser.us_senha = usuario.senha
        sysuser.us_complex = usuario.complex
        sysuser.us_senhaNova = usuario.senhaNova
        sysuser.us_hashNovaSenha = usuario.hashSenhaNova

        DB.session.commit()
        return True
        


