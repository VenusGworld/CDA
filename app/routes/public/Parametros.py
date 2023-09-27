from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from flask import Blueprint, render_template, request, Response, abort, flash
from ...extensions.LogErro import LogErro
import traceback
import sys
import json

parametrosBlue = Blueprint("parametrosBlue", __name__)

##################################################################
# Rotas relacionadas as funcionalidades dos parãmetros do sistema
#################################################################

#Rota para tela de alteração de parametros do sistema
@parametrosBlue.route("/admin/parametros", methods=['GET'])
def parametros():
    try:
        controleconsultaParametros = ControleConsultaParametros()
        parametros = controleconsultaParametros.consultaTodosParametros()
        context = {"titulo": "Parâmetros do Sistema", "active": "parametros", "parms": parametros}
        return render_template("administrador/parametros/parametros.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para alterar os parametros das telas de consultas
@parametrosBlue.route("/altera-parametros", methods=['POST'])
def aletraParametros():
    try:
        data = request.get_json()
        controleconsultaParametros = ControleConsultaParametros()
        controleconsultaParametros.aletarParametros(data["inputs"])
        flash("Parâmetro(s) alterado(s) com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True }), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        resp = Response(status=500, mimetype="application/json")
        return resp
