from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleConsultarLogTerc import ControleConsultarLogTerc
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logTercTecBlue = Blueprint("logTercTecBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do CRUD de terceiro
##############################################################

#Rota para tela de log de terceiro
@logTercTecBlue.route("/log/log-manter-terceiro")
@login_required
def listagemLogTerceiro():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_LOG_MANT_TERC")
        context = {"titulo": "Logs Manter Terceiro", "active": "logTerc", "meses": meses}
        return render_template("tecAdm/cosultaLogTerceiro.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela com modal para visualização detalhada dos logs de terceiros
@logTercTecBlue.route("/log/log-manter-terceiro/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controleConsultarTerc = ControleConsultarLogTerc()
        log = controleConsultarTerc.consultaLogTercDetelhado(int(id))
        if log.acao == "INSERT":
            modal = 1
        elif log.acao == "UPDATE":
            modal = 2
        elif log.acao in ["DELETE", "ACTIVE"]:
            modal = 3
        context = {"titulo": "Logs Manter Terceiro", "active": "logTerc", "modal": modal, "log": log}
        return render_template("tecAdm/cosultaLogTerceiro.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)