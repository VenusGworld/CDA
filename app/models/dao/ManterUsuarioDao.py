from ...configurations.Database import DB
from configparser import ConfigParser
from ..entity.Usuario import Usuario
from ..Tables import SysUser
import os

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

        sysusers = SysUser.query.filter(SysUser.us_ativo!=True, SysUser.us_delete!=True)
        for sysuser in sysusers:
            user = Usuario()
            user.id = sysuser.id
            user.nome = sysuser.us_nome
            user.email = sysuser.us_email
            user.usuario = sysuser.us_usuario
            user.senha = sysuser.us_senha
            user.grupo = sysuser.us_grupo
            user.ativo = sysuser.us_ativo
            user.delete = sysuser.us_delete
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
        usuario.id = sysuser.id
        usuario.nome = sysuser.us_nome
        usuario.email = sysuser.us_email
        usuario.usuario = sysuser.us_usuario
        usuario.senha = sysuser.us_senha
        usuario.complex = sysuser.us_complex
        usuario.grupo = sysuser.us_grupo
        usuario.ativo = sysuser.us_ativo
        usuario.delete = sysuser.us_delete
        
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

        if usuario.usuario != "ADMIN": #Verifica se o usuário para inserção é o ADMIN
            sysuser = SysUser(usuario=usuario.usuario, senha=usuario.senha,
                            email=usuario.email, nome=usuario.nome,
                            grupo=usuario.grupo, complex=usuario.complex,
                            hashNovaSenha=usuario.hashSenhaNova, senhaNova=usuario.senhaNova,
                            limiteNovaSenha="", ativo=usuario.ativo, delete=usuario.delete)
        else:
            sysuser = SysUser(usuario=usuario.usuario, senha=usuario.senhaCompara,
                            email=usuario.email, nome=usuario.nome,
                            grupo=usuario.grupo, complex=usuario.complex,
                            hashNovaSenha=usuario.hashSenhaNova, senhaNova=usuario.senhaNova,
                            limiteNovaSenha="", ativo=usuario.ativo, delete=usuario.delete)
            
        DB.session.add(sysuser)
        DB.session.commit()
        return True


    def editarUsuario(self, usuario: Usuario) -> bool:
        #########################################################################################
        # Essa Função altera um usuário.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com os dados para alterção.
        
        # RETORNOS:
        #   return True = Retorna True caso foi alterado com sucesso;
        #   return False = Retorna False caso ocorra erro na alteração.
        #########################################################################################

        sysuser = SysUser.query.get(usuario.id)
        sysuser.us_nome = usuario.nome
        sysuser.us_email = usuario.email
        sysuser.us_usuario = usuario.usuario
        sysuser.us_senha = usuario.senha
        sysuser.us_grupo = usuario.grupo
        sysuser.us_complex = usuario.complex
        sysuser.us_ativo = usuario.ativo
        sysuser.us_delete = usuario.delete

        DB.session.commit()
        return True
        
        

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

        DB.session.commit()
        return True
       
        
    def inativarUsuario(self, id: int) -> bool:
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
        
        DB.session.commit()
        return True
        


    def adicionarAdm(self, usuario: Usuario):
        #########################################################################################
        # Essa Função acessa o arquivo .ini para completar os dados do usuário ADMIN.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario para completar os dados que estão no arquivo.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        arquivo = ConfigParser()
        arquivo.read(f"{os.path.dirname(os.path.realpath(__file__))}/variaveis/auth.ini")
        
        usuario.nome = arquivo.get("MasterUser", "usuario")
        usuario.senhaCompara = arquivo.get("MasterUser", "senha")
        usuario.complex = arquivo.get("MasterUser", "complex")
        usuario.nome = arquivo.get("MasterUser", "nome")
        usuario.email = arquivo.get("MasterUser", "email")
        usuario.grupo = arquivo.get("MasterUser", "grupo")
        usuario.hashSenhaNova = ''
        usuario.senhaNova = False 
        usuario.ativo = False
        usuario.delete = False
