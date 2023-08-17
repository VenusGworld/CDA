from flask import Blueprint, render_template, request, abort, Response
from ...controllers.ControleMensagem import ControleMensagem
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import json
import sys


mensagemAdmBlue = Blueprint("mensagemAdmBlue", __name__)

##############################################################
# Rotas relacionadas ao enviar mensagem
##############################################################

#Rota para a tela de Enviar Mensagem
@mensagemAdmBlue.route('/mensagem/enviar-mensagem', methods=["GET"])
@login_required
def enviarMensagem():
    try:
        controleMensagem = ControleMensagem()
        grupos = controleMensagem.consultaMaquinas()
        context = {"titulo": "Enviar Mensagem", "active": "mansagem", "grupos": grupos}
        return render_template("administrador/mensagem/mensagem.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para enviar mensagem
@mensagemAdmBlue.route('/mensagem/enviar-mensagem', methods=["POST"])
@login_required
def sendMensagem():
    try:
        data = request.get_json()
        controleMensagem = ControleMensagem()
        controleMensagem.enviarMesagem(data["mensagem"], data["destinos"])
        resp = Response(response=json.dumps({"secsses": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        resp = Response(status=500, mimetype="application/json")
        return resp