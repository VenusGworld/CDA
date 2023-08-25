from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..extensions.EnviarMensagem import Mensagem
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from ..models.dao.Ldap import Ldap
from datetime import datetime
from flask import session

class ControleMensagem:
    """
    Classe Controller para as funções recionadas ao enviar mensagem
    @author - Fabio
    @version - 1.0
    @since - 20/06/2023
"""

    def consultaMaquinas(self) -> dict:
        """
        Essa função consulta no Active Directory(AD) e retorna um dicionário com os grupos de máquinas associadas a determinado setor.

        :return: Um dicionário contendo grupos de máquinas e suas respectivas máquinas.
        """
        
        ldap = Ldap()
        grupos = ["Almoxarifado", "Cobranca", "Compras", "Contabil", "CPD", "Diretoria", "Fabrica", "Faturamento", "Financeiro", "Fiscal", "Lab Algodao", "Lab Fios", "Manutencao", "PCP", "Portaria", "RH", "Secretaria", "Sesmt", "Vendas"]

        listaGrupos = []
        for grupo in grupos:
            listaMaquinas = []
            
            for maquina in ldap.consultarMaquinas(grupo):
                listaMaquinas.append(maquina["attributes"]["cn"])

            
            listaGrupos.append({
                            "nome": grupo,
                            "maquinas": listaMaquinas
                            })

            dicGrupo = {
                "grupos": listaGrupos
            }

        return dicGrupo
    

    def enviarMesagem(self, mensagem: str, destinos: list[str]) -> bool:
        """
        Envia uma mensagem para uma lista de destinos(máquinas).

        :param mensagem: A mensagem a ser enviada.
        :param destinos: Uma lista de strings contendo os destinos(máquinas) para enviar a mensagem.
        """

        enviarMensagem = Mensagem()
        for maquina in destinos:
            enviarMensagem.enviarMensagem(mensagem.upper(), maquina)

        consultaIdUser = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
        self.geraLogMensagem(mensagem)

        return True
    

    def geraLogMensagem(self, mensagem: str) -> None:
        """
        Gera um registro de log para ações relacionadas ao enviar mensagem.

        :param mensagem: mensagem que foi enviada.

        :return: Nenhum valor é retornado.
        """

        log = Log()
        log.acao = ""
        log.dataHora = datetime.now()
        log.observacao = mensagem.upper()
        log.usuario = self.usuarioLogado
        log.dadosAntigos = {"vazio": 0}
        log.dadosNovos = {"vazio": 0}


        logDao = GeraLogDao()
        logDao.inserirLogMensagem(log)
