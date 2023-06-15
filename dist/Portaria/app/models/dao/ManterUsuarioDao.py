from ..entity.Usuario import Usuario
from ..Tables import SysUser
from ...extensions.Database import DB
import sys

class ManterUsuarioDao:

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


