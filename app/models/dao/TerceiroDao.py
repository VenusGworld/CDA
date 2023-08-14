from ..Tables import CDA016

"""
Classe Dao para a tabela de relacionamento de movimento de terceiro e terceiro
@tables - CDA016
@author - Fabio
@version - 1.0
@since - 09/08/2023
"""

class TerceiroDao:

    def terceirosMovimento(self, idMov: int) -> list[int]:
        ids = CDA016.query.filter(CDA016.id_movTerc==idMov)
        
        listaIds = []
        if ids:    
            for id in ids:
                listaIds.append(id.id_terceiro)
            return listaIds
        else:
            return listaIds