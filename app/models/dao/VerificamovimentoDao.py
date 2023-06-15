from ..entity.Usuario import Usuario
from ..Tables import SysUser, CDA013, CDA008, CDA012, CDA006, CDA011, CDA010, CDA001, CDA014
from ...extensions.Database import DB
import sys


class VerificaMovimentoDao:

    def verificaMovimentoUsuario(self, id: int) -> bool:
        movimento = 0
        if CDA013.query.filter(CDA013.lus_idUsua==id).first():
            movimento += 1

        if CDA008.query.filter(CDA008.lmte_idUsua==id).first():
            movimento += 1

        if CDA012.query.filter(CDA012.lte_idUsua==id).first():
            movimento += 1

        if CDA006.query.filter(CDA006.lmge_idUsua==id).first():
            movimento += 1

        if CDA011.query.filter(CDA011.lge_idUsua==id).first():
            movimento += 1

        if CDA010.query.filter(CDA010.lch_idUsua==id).first():
            movimento += 1

        if CDA011.query.filter(CDA011.lge_idUsua==id).first():
            movimento += 1

        if CDA014.query.filter(CDA014.lme_idUsua==id).first():
            movimento += 1

        if movimento == 0:
            return False
        else:
            return True