from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleConsultarLogFunc import ControleConsultarLogFunc
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logFuncAdmBlue = Blueprint("logFuncAdmBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do CRUD de Funcionários
##############################################################

#Rota para tela de log de Funcionários
@logFuncAdmBlue.route("/log/log-manter-funcionario", methods=["GET"])
@login_required
def listagemLogFunc():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_LOG_MANT_FUNC")
        context = {"titulo": "Logs Manter Funcionário", "active": "logFunc", "meses": meses}
        return render_template("administrador/logFuncionario/cosultaLogFunc.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de log de Funcionários
@logFuncAdmBlue.route("/log/log-manter-funcionario/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controleConsultaLogFunc = ControleConsultarLogFunc()
        log = controleConsultaLogFunc.consultaLogFuncInsertDetelhado(id)
        if log.acao == "INSERT":
            modal = 1
        elif log.acao == "UPDATE":
            modal = 2
        elif log.acao in ["DELETE", "ACTIVE"]:
            modal = 3
        context = {"titulo": "Logs Manter Funcionário", "active": "logFunc", "modal": modal, "log": log}
        return render_template("administrador/logFuncionario/cosultaLogFunc.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)