from ...controllers.ControleConsultarLogControlTerc import ControleConsultarLogControlTerc
from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logControlTercTecBlue = Blueprint("logControlTercTecBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do controle de terceiros
##############################################################

#Rota para tela de log do controle de terceiros
@logControlTercTecBlue.route("/log/log-controle-terceiro", methods=["GET"])
@login_required
def listagemLogControlTerc():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_LOG_MANT_CHAV")
        context = {"titulo": "Logs Controle de Terceiro", "active": "logControlTerc", "meses": meses}
        return render_template("tecAdm/consultaLogControlTerc.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela com modal para visualização detalhada dos logs do controle de terceiros
@logControlTercTecBlue.route("/log/log-controle-terceiro/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controlerConsultaLogControlterc = ControleConsultarLogControlTerc()
        log = controlerConsultaLogControlterc.consultaLogControlTercDetelhado(int(id))
        if log.acao == "ENTRADA":
            modal = 1
        elif log.acao == "SAIDA":
            modal = 2
        elif log.acao == "UPDATE":
            modal = 3
        elif log.acao == "DELETE":
            modal = 4
        context = {"titulo": "Logs Controle de Terceiro", "active": "logControlTerc", "modal": modal, "log": log}
        return render_template("tecAdm/consultaLogControlTerc.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)