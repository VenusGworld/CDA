from ...configurations.Database import DB
from configparser import ConfigParser
from ..entity.Usuario import Usuario
from ..Tables import SysUser
import os


class ManterUsuarioDao:
    """
    Classe Dao para CRUD do usuário
    @tables - SysUser
    @author - Fabio
    @version - 1.0
    @since - 05/06/2023
    """

    def consultarUsuarios(self) -> list[Usuario]:
        """
        Consulta os usuários que não estão inativos ou deletados cadastradas no sistema.

        :return: Uma lista de usuário.
        """

        lisUsuarios = []

        sysusers = SysUser.query.filter(SysUser.us_inativo!=True, SysUser.us_delete!=True)
        for sysuser in sysusers:
            user = Usuario(id=sysuser.id, nome=sysuser.us_nome, email=sysuser.us_email, usuario=sysuser.us_usuario,
                          senha=sysuser.us_senha, complex=sysuser.us_complex, grupo=sysuser.us_grupo, ativo=sysuser.us_inativo,
                          delete=sysuser.us_delete)
            lisUsuarios.append(user)

        return lisUsuarios
    

    def consultarUsuarioDetalhado(self, id: int) -> Usuario:
        """
        Consulta os detalhes de um usuário no sistema.

        :param id: O ID do usuário a ser consultado.

        :return: Objeto 'Usuario' contendo as informações detalhadas do usuário.
        """

        sysuser = SysUser.query.get(id)
        usuario = Usuario(id=sysuser.id, nome=sysuser.us_nome, email=sysuser.us_email, usuario=sysuser.us_usuario,
                          senha=sysuser.us_senha, complex=sysuser.us_complex, grupo=sysuser.us_grupo, ativo=sysuser.us_inativo,
                          delete=sysuser.us_delete)
        
        return usuario
    

    def inserirUsuario(self, usuario: Usuario) -> bool:
        """
        Insere um novo usuário no sistema.

        :param usuario: Objeto 'Usuario' contendo informações do novo usuário.

        :return: True se o processo de inserção for bem-sucedido, False caso contrário.
        """

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
        """
        Edita as informações de um usuário no banco de dados.

        :param usuario: Objeto da classe Usuario contendo as novas informações do usuário.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        sysuser = SysUser.query.get(usuario.id)
        sysuser.us_nome = usuario.nome
        sysuser.us_email = usuario.email
        sysuser.us_usuario = usuario.usuario
        sysuser.us_senha = usuario.senha
        sysuser.us_grupo = usuario.grupo
        sysuser.us_complex = usuario.complex
        sysuser.us_inativo = usuario.ativo
        sysuser.us_delete = usuario.delete

        DB.session.commit()
        return True
          

    def excluirUsuario(self, id: int) -> bool:
        """
        Marca um usuário como excluído no sistema.

        :param id: ID do usuário a ser marcado como excluído.

        :return: True se a marcação como excluído for bem-sucedida, False caso contrário.
        """

        sysuser = SysUser.query.get(id)
        sysuser.us_delete = True

        DB.session.commit()
        return True
       
        
    def inativarUsuario(self, id: int) -> bool:
        """
        Marca um usuário como desativado no sistema.

        :param id: ID do usuário a ser marcado como desativado.
        
        :return: True se a marcação como desativado for bem-sucedida, False caso contrário.
        """

        sysuser = SysUser.query.get(id)
        sysuser.us_inativo = True
        
        DB.session.commit()
        return True
        

    def adicionarAdm(self, usuario: Usuario):
        """
        Adiciona um usuário administrador baseado em informações do arquivo de configuração.

        :param usuario: O objeto 'Usuario' ao qual as informações do usuário administrador serão atribuídas.
        
        :return: Nenhum valor é retornado. As informações do usuário administrador são preenchidas no objeto 'usuario'.
        """

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
