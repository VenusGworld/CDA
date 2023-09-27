from ..Tables import CDA005, CDA007, CDA002, CDA009, CDA003, SysUser
from ldap3 import Server, Connection
from typing import Optional

class PesquisaDao:
    """
    Classe Dao para pesquisas do sistema
    @tables - CDA005, CDA007, CDA002, CDA009, CDA003, SysUser
    @author - Fabio
    @version - 1.0
    @since - 05/06/2023
    """

    def pesquisaChaveNomeDao(self, nome: str, considerarInativos: Optional[bool] = True) -> CDA005:
        """
        Esta função realiza uma pesquisa na tabela de chaves (CDA005) utilizando o nome fornecido como filtro.
        Ela utiliza o operador SQL 'LIKE' para buscar chaves cujo nome contenha a substring especificada.
        Os resultados são filtrados para excluir chaves deletadas (ch_delete) e chaves inativas (ch_inativo).
        
        :param nome: O nome ou parte do nome da chave a ser pesquisada.
        :param considerar_inativos: Indica se os registros inativos devem ser considerados na pesquisa. 
                                    O padrão é True, o que significa que os inativos são considerados.

        :return: Uma lista de chaves que correspondem aos critérios de pesquisa.
        """

        if considerarInativos:
            chaves = CDA005.query.filter(CDA005.ch_nome.like(f"%{nome}%"), CDA005.ch_delete!=True, CDA005.ch_inativo!=True)
        else:
            chaves = CDA005.query.filter(CDA005.ch_nome.like(f"%{nome}%"), CDA005.ch_delete!=True)

        return chaves
    

    def pesquisaChaveCodigoDao(self, codigo: str, considerarInativos: Optional[bool] = True) -> CDA005:
        """
        Esta função realiza uma pesquisa na tabela de chaves (CDA005) utilizando o código fornecido como filtro.
        Ela utiliza o operador SQL 'LIKE' para buscar chaves cujo código contenha a substring especificada.
        Os resultados são filtrados para excluir chaves deletadas (ch_delete) e chaves inativas (ch_inativo).
        
        :param codigo: O código ou parte do código da chave a ser pesquisada.
        :param considerar_inativos: Indica se os registros inativos devem ser considerados na pesquisa. 
                                    O padrão é True, o que significa que os inativos são considerados.

        :return: Uma lista de chaves que correspondem aos critérios de pesquisa.
        """

        if considerarInativos:
            chaves = CDA005.query.filter(CDA005.ch_codigo.like(f"%{codigo}%"), CDA005.ch_delete!=True, CDA005.ch_inativo!=True)
        else:
            chaves = CDA005.query.filter(CDA005.ch_codigo.like(f"%{codigo}%"), CDA005.ch_delete!=True)

        return chaves
    

    def pesquisaFuncNomeChaveDao(self, nome: str) -> CDA007:
        """
        Esta função realiza uma pesquisa na tabela de funcionários (CDA007) utilizando o nome fornecido como filtro.
        Ela utiliza o operador SQL 'LIKE' para buscar funcionários cujo nome contenha a substring especificada.
        Os resultados são filtrados para excluir funcionários deletados (fu_delete) e funcionários inativos (fu_inativo).
        
        :param nome: O nome ou parte do nome do funcionário a ser pesquisado.

        :return: Uma lista de funcionários que correspondem aos critérios de pesquisa.
        """

        funcionarios = CDA007.query.filter(CDA007.fu_nome.like(f"%{nome}%"), CDA007.fu_delete!=True, CDA007.fu_inativo!=True)

        return funcionarios
    
    
    def pesquisaFuncCrachaChaveDao(self, cracha: str) -> CDA007:
        """
        Esta função realiza uma pesquisa na tabela de funcionários (CDA007) utilizando o número do crachá fornecido como filtro.
        Ela utiliza o operador SQL 'LIKE' para buscar funcionários cujo número do crachá contenha a substring especificada.
        Os resultados são filtrados para excluir funcionários deletados (fu_delete) e funcionários inativos (fu_inativo).
        
        :param cracha: O número do crachá ou parte do número do crachá do funcionário a ser pesquisado.

        :return: Uma lista de funcionários que correspondem aos critérios de pesquisa.
        """

        funcionarios = CDA007.query.filter(CDA007.fu_cracha.like(f"%{cracha}%"), CDA007.fu_delete!=True, CDA007.fu_inativo!=True)

        return funcionarios
    
    
    def pesquisaCpfTerc(self, cpf: str) -> CDA009:
        """
        Esta função realiza uma pesquisa na tabela de terceiros (CDA009) utilizando o número de CPF fornecido como filtro.
        Ela utiliza o operador SQL 'LIKE' para buscar terceiros cujo número de CPF contenha a substring especificada.
        Os resultados são filtrados para excluir terceiros deletados (te_delete) e terceiros inativos (te_inativo).
        
        :param cpf: O número de CPF ou parte do número de CPF do terceiro a ser pesquisado.

        :return: Uma lista de terceiros que correspondem aos critérios de pesquisa.
        """

        terceiros = CDA009.query.filter(CDA009.te_cpf.like(f"%{cpf}%"), CDA009.te_delete!=True, CDA009.te_inativo!=True)

        return terceiros
    

    def pesquisaCrachaFormDao(self, cracha: str, id: int) -> CDA007:
        """
        Esta função realiza uma pesquisa na tabela de funcionários (CDA007) utilizando o número de crachá fornecido como filtro.
        Ela também exclui o funcionário com o ID especificado da pesquisa.
        
        :param cracha: O número de crachá do funcionário a ser pesquisado.
        :param id: O ID do funcionário a ser excluído da pesquisa.

        :return: O funcionário correspondente ao número de crachá, excluindo o funcionário com o ID fornecido.
        """

        crachaFunc = CDA007.query.filter(CDA007.fu_cracha==cracha, CDA007.id_funcionario!=id).first()

        return crachaFunc
    
    
    def pesquisaMaquinasFormDao(self) -> list:
        """
        Esta função se conecta ao servidor LDAP e realiza uma pesquisa para obter informações sobre as máquinas disponíveis.
        Ela retorna uma lista de máquinas encontradas, incluindo seus nomes e outros atributos relevantes.

        :return: Uma lista de máquinas disponíveis, incluindo seus nomes e atributos.
        """

        conn = Connection(Server(''),
                            auto_bind=True,
                            user="{}\\{}".format("", ""),
                            password="",
                            auto_referrals=False)

        maquinas = conn.extend.standard.paged_search(f'', '(objectClass=computer)', attributes=['cn', 'givenName'])

        return maquinas
    

    def pesquisaUsuarioFormDao(self, usuario: str, id: int) -> SysUser:
        """
        Esta função consulta o banco de dados para verificar se um nome de usuário específico já está sendo usado
        por outro usuário, excluindo o usuário com o ID fornecido. Ela retorna o usuário encontrado, se houver,
        ou None se o nome de usuário estiver disponível.

        :param usuario: O nome de usuário que está sendo verificado.
        :param id: O ID do usuário que está sendo editado, para que esse usuário seja excluído da pesquisa.

        :return: O usuário encontrado com o nome de usuário, ou None se o nome de usuário estiver disponível.
        """

        user = SysUser.query.filter(SysUser.us_usuario==usuario, SysUser.id!=id).first()

        return user
    

    def pesquisaChaveFormMovDao(self, codigo: str) -> CDA005:
        """
        Esta função consulta o banco de dados para verificar se um código de chave específico já está sendo usado
        por outra chave. Ela retorna a chave encontrada, se houver, ou None se o código de chave estiver disponível.

        :param codigo: O código de chave que está sendo verificado.

        :return: A chave encontrada com o código de chave, ou None se o código de chave estiver disponível.
        """

        chave = CDA005.query.filter(CDA005.ch_codigo==codigo, CDA005.ch_delete!=True, CDA005.ch_inativo!=True).first()

        return chave
    

    def pesquisaFuncFormMovDao(self, cracha: str) -> CDA005:
        """
        Esta função consulta o banco de dados para verificar se um crachá específico já está sendo usado
        por outro funcionário. Ela retorna o funcionário encontrado, se houver, ou None se o crachá estiver disponível.

        :param cracha: O número de crachá que está sendo verificado.

        :return: O funcionário encontrado com o número de crachá, ou None se o crachá estiver disponível.
        """

        funcionario = CDA007.query.filter(CDA007.fu_cracha==cracha, CDA007.fu_delete!=True, CDA007.fu_inativo!=True).first()

        return funcionario
    

    def pesquisaChaveRetFormMovDao(self, id: int) -> CDA002:
        """
        Esta função consulta o banco de dados para verificar se há um movimento de devolução de chave aberto
        para uma chave específica. Ela retorna o movimento de devolução encontrado, se houver, ou None
        se não houver nenhum movimento aberto para a chave.

        :param id: O ID da chave para a qual se deseja verificar a devolução.

        :return: O movimento de devolução encontrado, ou None se não houver movimento aberto para a chave.
        """
        
        movimento = CDA002.query.filter(CDA002.mch_idChav==id, CDA002.mch_dataDev==None, CDA002.mch_horaDev==None, CDA002.mch_delete!=True).first()

        return movimento
    

    def pesquisaCpfTercFormMov(self, cpf: str) -> CDA009:
        """
        Esta função consulta o banco de dados para verificar se há um terceiro registrado com o CPF fornecido.
        Ela retorna o terceiro encontrado, se houver, ou None se não houver nenhum terceiro registrado com o CPF.

        :param cpf: O CPF do terceiro que se deseja pesquisar.

        :return: O terceiro encontrado, ou None se não houver terceiro registrado com o CPF.
        """

        terceiro = CDA009.query.filter(CDA009.te_cpf==cpf, CDA009.te_delete!=True, CDA009.te_inativo!=True).first()

        return terceiro
    

    def pesquisaGerNomeMovDao(self, nome: str, considerarInativos: Optional[bool] = True) -> CDA007:
        """
        Esta função consulta o banco de dados para verificar se há gerentes de funcionários registrados com o nome fornecido.
        Ela retorna uma lista de gerentes encontrados, se houver, ou uma lista vazia se não houver nenhum gerente registrado com o nome.

        :param nome: O nome do gerente de funcionários que se deseja pesquisar.
        :param considerar_inativos: Indica se os registros inativos devem ser considerados na pesquisa. 
                                    O padrão é True, o que significa que os inativos são considerados.

        :return: Uma lista de gerentes de funcionários encontrados, ou uma lista vazia se não houver gerentes com o nome especificado.
        """

        if considerarInativos:
            gerentes = CDA007.query.filter(CDA007.fu_nome.like(f"%{nome}%"), CDA007.fu_delete!=True, CDA007.fu_inativo!=True, CDA007.fu_gerente==True)
        else:
            gerentes = CDA007.query.filter(CDA007.fu_nome.like(f"%{nome}%"), CDA007.fu_delete!=True, CDA007.fu_gerente==True)

        return gerentes
    
    
    def pesquisaGerCrachaMovDao(self, cracha: str, considerarInativos: Optional[bool] = True) -> CDA007:
        """
        Esta função consulta o banco de dados para verificar se há gerentes de funcionários registrados com o número de crachá fornecido.
        Ela retorna uma lista de gerentes encontrados, se houver, ou uma lista vazia se não houver nenhum gerente registrado com o número de crachá.

        :param cracha: O número de crachá do gerente de funcionários que se deseja pesquisar.
        :param considerar_inativos: Indica se os registros inativos devem ser considerados na pesquisa. 
                                    O padrão é True, o que significa que os inativos são considerados.
        
        :return: Uma lista de gerentes de funcionários encontrados, ou uma lista vazia se não houver gerentes com o número de crachá especificado.
        """

        if considerarInativos:
            gerentes = CDA007.query.filter(CDA007.fu_cracha.like(f"%{cracha}%"), CDA007.fu_delete!=True, CDA007.fu_inativo!=True, CDA007.fu_gerente==True)
        else:
            gerentes = CDA007.query.filter(CDA007.fu_cracha.like(f"%{cracha}%"), CDA007.fu_delete!=True, CDA007.fu_gerente==True)

        return gerentes
    

    def pesquisaGerenteSaiFormMovDao(self, id: int) -> CDA003:
        """
        Esta função consulta o banco de dados para verificar se há um registro de movimento de saída não concluído de um gerente de funcionários com o ID especificado.
        Ela retorna o primeiro registro de movimento de saída não concluído encontrado, se houver, ou None se não houver nenhum registro correspondente.

        :param id: O ID do gerente de funcionários para o qual se deseja pesquisar o movimento de saída não concluído.

        :return: O registro de movimento de saída não concluído encontrado, ou None se não houver nenhum registro correspondente.
        """

        movimento = CDA003.query.filter(CDA003.mge_idFunc==id, CDA003.mge_dataSaid==None, CDA003.mge_horaSaid==None, CDA003.mge_delete!=True).first()

        return movimento