from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleConsultarLogControlChav import ControleConsultarLogControlChav
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logControlChavTecBlue = Blueprint("logControlChavTecBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do controle de chaves
##############################################################

#Rota para tela de log de controle de chaves
@logControlChavTecBlue.route("/log/log-controle-chave", methods=["GET"])
@login_required
def listagemLogControlChave():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_MANUT_CONTROL_CHAV")
        context = {"titulo": "Logs Controle de Chave", "active": "logControlChav", "meses": meses}
        return render_template("tecAdm/consultaLogControlChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela com modal para visualização detalhada dos logs de controle de chaves
@logControlChavTecBlue.route("/log/log-controle-chave/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controleConusltaLogControlChav = ControleConsultarLogControlChav()
        log = controleConusltaLogControlChav.consultaLogControlChaveDetelhado(int(id))
        if log.acao == "RETIRADA":
            modal = 1
        elif log.acao == "DEVOLUCAO":
            modal = 2
        elif log.acao == "UPDATE":
            modal = 3
        elif log.acao == "DELETE":
            modal = 4
        context = {"titulo": "Logs Controle de Chave", "active": "logControlChav", "modal": modal, "log": log}
        return render_template("tecAdm/consultaLogControlChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)