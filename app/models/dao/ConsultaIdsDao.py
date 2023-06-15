from ..Tables import *
from ...extensions.Database import DB

class ConsultaIds:

    def consultaIdUserLogado(self, usuario: str) -> int:
        id = DB.session.query(SysUser.id).filter(SysUser.us_usuario==usuario).order_by(SysUser.id.desc()).first()
        return id[0]
    
    def consultaIdFinalUser(self) -> int:
        id = DB.session.query(SysUser.id).order_by(SysUser.id.desc()).first()
        return id[0]

    