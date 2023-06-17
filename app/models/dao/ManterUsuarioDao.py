from ..entity.Usuario import Usuario
from ..Tables import SysUser
from ...extensions.Database import DB
import sys
import os
from configparser import ConfigParser

"""
Classe Dao para CRUD do usuário
@tables - SysUser
@author - Fabio
@version - 1.0
@since - 05/06/2023
"""

class ManterUsuarioDao:

    def mostarUsuarios(self) -> list[Usuario]:
        #########################################################################################
        # Essa Função retorna uma lista contendo os usuários que não estão deletados/inativos.
        
        # PARAMETROS:
        #   Não tem parametro.
        
        # RETORNOS:
        #   return lisUsuarios = Retorna a lista contendo os usuários.
        #########################################################################################

        lisUsuarios = []

        sysusers = SysUser.query.filter(SysUser.us_ativo!=1, SysUser.us_delete!=1).all()
        for sysuser in sysusers:
            user = Usuario()
            user.set_id(sysuser.id)
            user.set_nome(sysuser.us_nome)
            user.set_email(sysuser.us_email)
            user.set_usuario(sysuser.us_usuario)
            user.set_senha(sysuser.us_senha)
            user.set_grupo(sysuser.us_grupo)
            user.set_ativo(sysuser.us_ativo)
            user.set_delete(sysuser.us_delete)
            lisUsuarios.append(user)
        return lisUsuarios
    

    def mostarUsuarioDetalhado(self, id: int) -> Usuario:
        #########################################################################################
        # Essa Função retorna os dados detalhados do usuário que foi passado.
        
        # PARAMETROS:
        #    id = ID do usuário selecionado.
        
        # RETORNOS:
        #   return usuario = Retorna a instancia da classe Usuario com os dados do banco.
        #########################################################################################

        sysuser = SysUser.query.get(id)
        
        usuario = Usuario()
        usuario.set_id(sysuser.id)
        usuario.set_nome(sysuser.us_nome)
        usuario.set_email(sysuser.us_email)
        usuario.set_usuario(sysuser.us_usuario)
        usuario.set_senha(sysuser.us_senha)
        usuario.set_complex(sysuser.us_complex)
        usuario.set_grupo(sysuser.us_grupo)
        usuario.set_ativo(sysuser.us_ativo)
        usuario.set_delete(sysuser.us_delete)
        
        return usuario
    

    def inserirUsuario(self, usuario: Usuario) -> bool:
        #########################################################################################
        # Essa Função insere um usuário no banco.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com os dados para inserção.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso;
        #   return False = Retorna False caso ocorra erro na inserção.
        #########################################################################################

        if usuario.get_usuario() != "ADMIN": #Verifica se o usuário para inserção é o ADMIN
            sysuser = SysUser(usuario=usuario.get_usuario(), senha=usuario.get_senha(),
                            email=usuario.get_email(), nome=usuario.get_nome(),
                            grupo=usuario.get_grupo(), complex=usuario.get_complex(),
                            hashNovaSenha=usuario.get_hashSenhaNova(), senhaNova=usuario.get_senhaNova(),
                            ativo=usuario.get_ativo(), delete=usuario.get_delete())
        else:
            sysuser = SysUser(usuario=usuario.get_usuario(), senha=usuario.get_senhaCompara(),
                            email=usuario.get_email(), nome=usuario.get_nome(),
                            grupo=usuario.get_grupo(), complex=usuario.get_complex(),
                            hashNovaSenha=usuario.get_hashSenhaNova(), senhaNova=usuario.get_senhaNova(),
                            ativo=usuario.get_ativo(), delete=usuario.get_delete())
            
        try:
            DB.session.add(sysuser)
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False


    def editarUsuario(self, usuario: Usuario) -> bool:
        #########################################################################################
        # Essa Função altera um usuário.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com os dados para alterção.
        
        # RETORNOS:
        #   return True = Retorna True caso foi alterado com sucesso;
        #   return False = Retorna False caso ocorra erro na alteração.
        #########################################################################################

        sysuser = SysUser.query.get(usuario.get_id())
        sysuser.us_nome = usuario.get_nome()
        sysuser.us_email = usuario.get_email()
        sysuser.us_usuario = usuario.get_usuario()
        sysuser.us_senha = usuario.get_senha()
        sysuser.us_grupo = usuario.get_grupo()
        sysuser.us_complex = usuario.get_complex()
        sysuser.us_ativo = usuario.get_ativo()
        sysuser.us_delete = usuario.get_delete()

        try:
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False
        

    def excluirUsuario(self, id: int) -> bool:
        #########################################################################################
        # Essa Função exclui o usuário.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com os dados para alterção.
        
        # RETORNOS:
        #   return True = Retorna True caso foi excluido com sucesso;
        #   return False = Retorna False caso ocorra erro na exclusão.
        #########################################################################################

        sysuser = SysUser.query.get(id)
        sysuser.us_delete = True

        try:
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False
        
    def inativaUsuario(self, id: int) -> bool:
        #########################################################################################
        # Essa Função inativa o usuário.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com os dados para alterção.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inativado com sucesso;
        #   return False = Retorna False caso ocorra erro na inativação.
        #########################################################################################

        sysuser = SysUser.query.get(id)
        sysuser.us_ativo = True
        
        try:
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False


    def adicionaAdm(self, usuario: Usuario):
        #########################################################################################
        # Essa Função acessa o arquivo .ini para completar os dados do usuário ADMIN.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario para completar os dados que estão no arquivo.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        arquivo = ConfigParser()
        arquivo.read(f"{os.path.dirname(os.path.realpath(__file__))}/variaveis/auth.ini")
        
        usuario.set_nome(arquivo.get("MasterUser", "usuario"))
        usuario.set_senhaCompara(arquivo.get("MasterUser", "senha"))
        usuario.set_complex(arquivo.get("MasterUser", "complex"))
        usuario.set_nome(arquivo.get("MasterUser", "nome"))
        usuario.set_email(arquivo.get("MasterUser", "email"))
        usuario.set_grupo(arquivo.get("MasterUser", "grupo"))
        usuario.set_hashSenhaNova('')
        usuario.set_senhaNova(False)
        usuario.set_ativo(False)
        usuario.set_delete(False)
