from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..extensions.EnviarMensagem import Mensagem
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from ..models.dao.Ldap import Ldap
from datetime import datetime
from flask import session


class ControleMensagem:

    def consultaMaquinas(self) -> dict:
        ldap = Ldap()
        grupos = ["Almoxarifado", "Cobranca", "Compras", "Contabil", "CPD", "Diretoria", "Fabrica", "Faturamento", "Financeiro", "Fiscal", "Lab Algodao", "Lab Fios", "Manutencao", "PCP", "Portaria", "RH", "Secretaria", "Sesmt", "Vendas"]

        listaGrupos = []
        for grupo in grupos:
            listaMaquinas = []
            
            for maquina in ldap.mostrarMaquinas(grupo):
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
        enviarMensagem = Mensagem()
        for maquina in destinos:
            enviarMensagem.enviarMensagem(mensagem.upper(), maquina)

        consultaIdUser = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
        self.geraLogMensagem(mensagem)

        return True
    

    def geraLogMensagem(self, mensagem: str) -> None:
        #########################################################################################
        # Essa função gera log do INSERT, UPDATE e DELETE do usuário.
        
        # PARAMETROS:
        #   acao = Ação que foi efetuada.
        
        # RETORNOS:
        #   Não tem retorno.
        #########################################################################################

        log = Log()
        log.acao = ""
        log.dataHora = datetime.now()
        log.observacao = mensagem.upper()
        log.usuario = self.usuarioLogado
        log.dadosAntigos = {"vazio": 0}
        log.dadosNovos = {"vazio": 0}


        logDao = GeraLogDao()
        logDao.inserirLogMensagem(log)
