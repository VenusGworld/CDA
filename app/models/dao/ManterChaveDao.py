from ...configurations.Database import DB
from ..entity.Chave import Chave
from ..Tables import CDA005


class ManterChaveDao:
    """
    Classe Dao para o manter Chave
    @tables - CDA005
    @author - Fabio
    @version - 1.0
    @since - 27/06/2023
    """

    def consultaChaves(self) -> CDA005:
        """
        Consulta as chaves que não estão inativas ou deletadas cadastradas no sistema.

        :return: Uma lista de chaves.
        """

        chaves = CDA005.query.filter(CDA005.ch_delete!=True, CDA005.ch_ativo!=True)

        return chaves


    def consultarChaveDetalhadaId(self, id: int) -> Chave:
        """
        Consulta os detalhes de uma chave pelo seu ID.

        :param id: O ID da chave a ser consultada.

        :return: Um objeto Chave contendo os detalhes da chave consultada.
        """

        chave = CDA005.query.filter(CDA005.id_chave==id).first()

        chav = Chave()
        chav.id = chave.id_chave
        chav.codigo = chave.ch_codigo
        chav.nome = chave.ch_nome
        chav.ativo = chave.ch_ativo
        chav.delete = chave.ch_delete

        return chav
    

    def consultarChaveDetalhadaCodigo(self, codigo: str) -> Chave:
        """
        Consulta os detalhes de uma chave pelo seu código.

        :param codigo: O código da chave a ser consultada.

        :return: Um objeto Chave contendo os detalhes da chave consultada.
        """

        chave = CDA005.query.filter(CDA005.ch_codigo==codigo).first()

        chav = Chave()
        chav.id = chave.id_chave
        chav.codigo = chave.ch_codigo
        chav.nome = chave.ch_nome
        chav.ativo = chave.ch_ativo
        chav.delete = chave.ch_delete

        return chav


    def consultaUltimoCodigo(self) -> str:
        """
        Consulta o último código de chave registrado.

        :return: O último código de chave registrado.
        """

        codigo = DB.session.query(CDA005.ch_codigo).order_by(CDA005.ch_codigo.desc()).first()
        
        return codigo


    def incluirChave(self, chave: Chave) -> bool:
        """
        Inclui uma nova chave no sistema.

        :param chave: Objeto do tipo Chave contendo informações da nova chave.

        :return: True se a inclusão for bem-sucedida, False caso contrário.
        """

        chav = CDA005(codigo=chave.codigo, nome=chave.nome, 
                      ativo=chave.ativo, delete=chave.delete)
        
        DB.session.add(chav)
        DB.session.commit()

        return True
    

    def editarChave(self, chave: Chave) -> bool:
        """
        Edita as informações de uma chave existente no sistema.

        :param chave: Objeto do tipo Chave contendo informações atualizadas da chave.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        chav = CDA005.query.get(chave.id)

        chav.ch_nome = chave.nome
        DB.session.commit()

        return True


    def excuirChave(self, id: int) -> bool:
        """
        Marca uma chave como excluída no sistema.

        :param id: ID da chave a ser marcada como excluída.

        :return: True se a marcação como excluída for bem-sucedida, False caso contrário.
        """

        chave = CDA005.query.get(id)

        chave.ch_delete = True
        DB.session.commit()

        return True


    def inativarChave(self, id: int) -> bool:
        """
        Marca uma chave como desativada no sistema.

        :param id: ID da chave a ser marcada como desativada.
        
        :return: True se a marcação como desativada for bem-sucedida, False caso contrário.
        """

        chave = CDA005.query.get(id)

        chave.ch_ativo = True
        DB.session.commit()
        
        return True
    

    def consultaUltimoId(self) -> int:
        """
        Consulta o último ID de chave registrado no sistema.

        :return: O último ID de chave registrado no sistema.
        """

        id = DB.session.query(CDA005.id_chave).order_by(CDA005.id_chave.desc()).first()

        return id[0]
    
    