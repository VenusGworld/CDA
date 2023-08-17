from flask import Blueprint, render_template, redirect, request, Response, session, url_for, abort, flash
from ...controllers.ControleGerente import ControleDeGerente
from ...extensions.LogErro import LogErro
from flask_login import login_required
from datetime import datetime
import traceback
import sys
import json


controleGerVigBlue = Blueprint("controleGerVigBlue", __name__)


#Rota para a tela de controle de gerentes
@controleGerVigBlue.route('/controle-gerente', methods=["GET"])
@login_required
def controleGerente():
    try:
        session["loginVig"] = False
        context = {"titulo": "Contorle de Gerente", "active": "controlGer"}
        return render_template("vigAdm/controleGerente/controleGerente.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de incluir entrada do gerente
@controleGerVigBlue.route('/controle-gerente/incluir-entrada', methods=["GET"])
@login_required
def incluirEntradaGer():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Entrada de Gerente", "active": "controlGer", "data": data}
            return render_template("vigAdm/controleGerente/incluirMovimentoGerente.html", context=context)
        else:
            return redirect(url_for('controleGerVigBlue.controleGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para incluir a entrada de gerente
@controleGerVigBlue.route('/controle-gerente/incluir-entrada', methods=["POST"])
@login_required
def insertEntradaGer():
    try:
        controleGerente = ControleDeGerente()
        if controleGerente.inserirEntrada(request.form["dtEnt"], request.form["hrEnt"], request.form["gerente"]):
            flash("Entrada incluida com sucesso!", "success")
            return redirect(url_for('controleGerVigBlue.controleGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de inclusão de saída de gerente
@controleGerVigBlue.route('/controle-gerente/incluir-saida-modal/<id>', methods=["GET"])
@login_required
def incluirSaidaGer(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleGerente = ControleDeGerente()
            movimento = controleGerente.consultaMovimentoDetalhado(id)
            data = datetime.now()
            context = {"active": "controlChav", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleGerente/controleGerente.html", context=context)
        else:
            return redirect(url_for('controleGerVigBlue.controleGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inclusão de saída de gerente
@controleGerVigBlue.route('/controle-gerente/incluir-saida', methods=["POST"])
@login_required
def insertSaidaGer():
    try:
        data = request.get_json()
        controleGerente = ControleDeGerente()
        controleGerente.inserirSaida(data["idMov"], data["dataSai"], data["horaSai"], data["crachaGer"])
        flash("Saída incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de manutenção de movimentação de gerentes
@controleGerVigBlue.route('/controle-gerente/manutencao-gerente', methods=["GET"])
@login_required
def manutencaoGerente():
    try:
        context = {"titulo": "Manutenção entrada e saída de Gerente", "active": "controlGer"}
        return render_template("vigAdm/controleGerente/manutencaoGerente.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)