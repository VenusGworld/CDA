from ..Tables import *
from ...extensions.Database import DB

class ConsultaIds:

    def consultaIdUsuario(self) -> int:
        id = DB.session.query(SysUser.id).order_by(SysUser.id.desc()).first()
        return id[0]
    