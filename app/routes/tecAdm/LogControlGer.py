from ...controllers.ControleConsultarLogControlGer import ControleConsultarLogControlGer
from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logControlGerTecBlue = Blueprint("logControlGerTecBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do controle de gerentes
##############################################################

#Rota para tela de log do controle de gerentes
@logControlGerTecBlue.route("/log/log-controle-gerente", methods=["GET"])
@login_required
def listagemLogControlGer():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_MANUT_CONTROL_GER")
        context = {"titulo": "Logs Controle de Gerente", "active": "logControlGere", "meses": meses}
        return render_template("tecAdm/consultaLogControlGer.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela com modal para visualização detalhada dos logs do controle de gerentes
@logControlGerTecBlue.route("/log/log-controle-gerente/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controlerConsultaLogControlGer = ControleConsultarLogControlGer()
        log = controlerConsultaLogControlGer.consultaLogControlGerDetelhado(int(id))
        if log.acao == "ENTRADA":
            modal = 1
        elif log.acao == "SAIDA":
            modal = 2
        elif log.acao == "UPDATE":
            modal = 3
        elif log.acao == "DELETE":
            modal = 4
        context = {"titulo": "Logs Controle de Gerente", "active": "logControlGere", "modal": modal, "log": log}
        return render_template("tecAdm/consultaLogControlGer.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)