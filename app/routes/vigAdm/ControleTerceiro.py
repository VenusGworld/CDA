from flask import Blueprint, render_template, redirect, request, Response, jsonify, session, url_for, abort, flash
from ...controllers.ControleTerceiro import ControleTerceiro
from ...extensions.LogErro import LogErro
from flask_login import login_required
from datetime import datetime
import traceback
import json
import sys

controleTercVigBlue = Blueprint("controleTercVigBlue", __name__)


#Rota para a tela de controle de Treceiros
@controleTercVigBlue.route('/controle-terceiro', methods=["GET"])
@login_required
def controleTerceiro():
    try:
        session["loginVig"] = False
        context = {"titulo": "Contorle de Terceiros", "active": "controlTerc"}
        return render_template("vigAdm/controleTerceiro/controleTerceiro.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de incluir entrada de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-entrada', methods=["GET"])
@login_required
def incluirEntradaTerc():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Entrada de Terceiro", "active": "controlTerc", "data": data}
            return render_template("vigAdm/controleTerceiro/incluirMovimentoTerceiro.html", context=context)
        else:
            return redirect(url_for('controleTercVigBlue.controleTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para incluir entrada de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-entrada', methods=["POST"])
@login_required
def insertEntradaTerc():
    try:
        dataJson = request.get_json()
        controleTerceiro = ControleTerceiro()
        controleTerceiro.inserirEntrada(dataJson["cpf"], dataJson["nome"], dataJson["empresa"], dataJson["placa"], dataJson["veiculo"], dataJson["motivo"], dataJson["pessoaVisit"], dataJson["dtEntrada"], dataJson["hrEntrada"], dataJson["acomps"])
        flash("Entrada de terceiro incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        resp = Response(response=json.dumps({"msg": "Error"}), status=500, mimetype="application/json")
        return resp
    

#Rota para modal de inclusão de saída de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-saida-modal/<id>', methods=["GET"])
@login_required
def incluirSaidaModalTerc(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleTerceiro = ControleTerceiro()
            movimento = controleTerceiro.consultaMovTercDetalhado(int(id))
            data = datetime.now()
            context = {"active": "controlTerc", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleTerceiro/controleTerceiro.html", context=context)
        else:
            return redirect(url_for('controleTercVigBlue.controleTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inclusão de saída de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-saida', methods=["POST"])
@login_required
def insertSaidaTerc():
    try:
        data = request.get_json()
        controleTerceiro = ControleTerceiro()
        controleTerceiro.inserirSaida(int(data["idMov"]), data["dataSaid"], data["horaSaid"], data["cpf"], data["acomps"], data["cracha"])
        flash("Saída incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)