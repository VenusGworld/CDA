from flask import Blueprint, render_template, redirect, request, Response, session, url_for, abort, flash
from ...controllers.ControleChave import CrontoleDeChave
from ...extensions.LogErro import LogErro
from flask_login import login_required
from datetime import datetime
import traceback
import json
import sys


controleChaveVigBlue = Blueprint("controleChaveVigBlue", __name__)


#Rota para a tela de controle de Chaves
@controleChaveVigBlue.route('/controle-chave', methods=["GET"])
@login_required
def controleChave():
    try:
        session["loginVig"] = False
        context = {"titulo": "Contorle de Chaves", "active": "controlChav"}
        return render_template("vigAdm/controleChave/controleChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de incluir retirada da Chave
@controleChaveVigBlue.route('/controle-chave/incluir-retirada', methods=["GET"])
@login_required
def incluirRetiradaChav():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Retirada de Chave", "active": "controlChav", "data": data}
            return render_template("vigAdm/controleChave/incluirMovimentoChave.html", context=context)
        else:
            return redirect(url_for('controleChaveVigBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para incluir a reirada da chave
@controleChaveVigBlue.route('/controle-chave/incluir-retirada', methods=["POST"])
@login_required
def insertRetiradaChav():
    try:
        controleChave = CrontoleDeChave()
        if controleChave.inserirRetirada(request.form["dtRet"], request.form["hrRet"], request.form["chave"], request.form["responsavel"]):
            flash("Retirada incluida com sucesso!", "success")
            return redirect(url_for("controleChaveVigBlue.controleChave"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de inclusão de devolução
@controleChaveVigBlue.route('/controle-chave/incluir-devolucao-modal/<id>', methods=["GET"])
@login_required
def incluirDevolucaoChav(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleChave = CrontoleDeChave()
            movimento = controleChave.consultaMovimentoDetalhado(id)
            data = datetime.now()
            context = {"active": "controlChav", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleChave/controleChave.html", context=context)
        else:
            return redirect(url_for('controleChaveVigBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inscluir a devolução de uma chave
@controleChaveVigBlue.route('/controle-chave/incluir-devolucao', methods=["POST"])
@login_required
def insertDevolucaoChav():
    try:
        data = request.get_json()
        controleChave = CrontoleDeChave()
        controleChave.inserirDevolucao(data["idMov"], data["dataDev"], data["horaDev"], data["respDev"], data["check"])
        flash("Devolução incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de manutenção da chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave', methods=["GET"])
@login_required
def manutencaoChave():
    try:
        context = {"titulo": "Manutenção retirada e devolução de Chave", "active": "controlChav"}
        return render_template("vigAdm/controleChave/manutencaoChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)