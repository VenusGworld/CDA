from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleConsultarLogChave import ControleConsultarLogChave
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logChavTecBlue = Blueprint("logChavTecBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do CRUD de chave
##############################################################

#Rota para tela de log de Chave
@logChavTecBlue.route("/log/log-manter-chave", methods=["GET"])
@login_required
def listagemLogChave():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_LOG_MANT_CHAV")
        context = {"titulo": "Logs Manter Chave", "active": "logChave", "meses": meses}
        return render_template("tecAdm/cosultaLogChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela com modal para visualização detalhada dos logs de chaves
@logChavTecBlue.route("/log/log-manter-chave/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controleConsultarLogChave = ControleConsultarLogChave()
        log = controleConsultarLogChave.consultaLogChaveDetelhado(int(id))
        if log.acao == "INSERT":
            modal = 1
        elif log.acao == "UPDATE":
            modal = 2
        elif log.acao in ["DELETE", "ACTIVE"]:
            modal = 3
        context = {"titulo": "Logs Manter Chave", "active": "logChave", "modal": modal, "log": log}
        return render_template("tecAdm/cosultaLogChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)