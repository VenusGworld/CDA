from ..entity.Usuario import Usuario
from ..Tables import SysUser
from ...extensions.Database import DB
import sys

class ManterUsuarioDao:

    def mostarUsuarios(self) -> list[Usuario]:
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
        sysuser = SysUser(usuario=usuario.get_usuario(), senha=usuario.get_senha(),
                          email=usuario.get_email(), nome=usuario.get_nome(),
                          grupo=usuario.get_grupo(), complex=usuario.get_complex(),
                          ativo=usuario.get_ativo(), delete=usuario.get_delete())
        try:
            DB.session.add(sysuser)
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False


    def editarUsuario(self, usuario: Usuario) -> bool:
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
        

    def excluirUsuario(self, id: int, ativoDelete: int) -> bool:
        sysuser = SysUser.query.get(id)
        if ativoDelete == 2:
            sysuser.us_ativo = True
        else: 
            sysuser.us_delete = True

        try:
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False
