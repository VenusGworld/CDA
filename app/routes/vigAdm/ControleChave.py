from flask import Blueprint, render_template, redirect, request, Response, jsonify, session, url_for, abort, flash
from flask_login import login_required
from ...controllers.ControleLogin import ControleLogin
from ...controllers.ControleChave import ControleCrontoleDeChave
from ...extensions.LogErro import LogErro
from datetime import datetime
import json
import sys
import traceback

controleChaveVigcBlue = Blueprint("controleChaveVigcBlue", __name__)


#Rota para a tela de controle de Chaves
@controleChaveVigcBlue.route('/controle-chave', methods=["GET"])
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
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela de incluir retirada da Chave
@controleChaveVigcBlue.route('/controle-chave/incluir-retirada', methods=["GET"])
@login_required
def incluirRetirada():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Retirada de Chave", "active": "controlChav", "data": data}
            return render_template("vigAdm/controleChave/incluirMovimentoChave.html", context=context)
        else:
            return redirect(url_for('controleChaveVigcBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para incluir a reirada da chave
@controleChaveVigcBlue.route('/controle-chave/incluir-retirada', methods=["POST"])
@login_required
def insertRetirada():
    try:
        controleChave = ControleCrontoleDeChave()
        if controleChave.inserirRetirada(request.form["dtRet"], request.form["hrRet"], request.form["chave"], request.form["responsavel"]):
            flash("Retirada incluida com sucesso!", "success")
            return redirect(url_for("controleChaveVigcBlue.controleChave"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para modal de inclusão de devolução
@controleChaveVigcBlue.route('/controle-chave/incluir-devolucao/<id>', methods=["GET"])
@login_required
def incluirDevolucao(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleChave = ControleCrontoleDeChave()
            movimento = controleChave.consultaMovimentoDetalhado(id)
            data = datetime.now()
            context = {"active": "controlChav", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleChave/controleChave.html", context=context)
        else:
            return redirect(url_for('controleChaveVigcBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para inscluir a devolução de uma chave
@controleChaveVigcBlue.route('/controle-chave/incluir-devolucao', methods=["POST"])
@login_required
def insertDevolucao():
    try:
        data = request.get_json()
        controleChave = ControleCrontoleDeChave()
        controleChave.inserirDevolucao(data["idMov"], data["dataDev"], data["horaDev"], data["respDev"], data["check"])
        flash("Devolução incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para tela de manutenção da chave
@controleChaveVigcBlue.route('/controle-chave/manutencao-chave', methods=["GET"])
@login_required
def manutencaoChave():
    try:
        context = {"titulo": "Manutenção retirada e devolução de Chave", "active": "controlChav"}
        return render_template("vigAdm/controleChave/manutencaoChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)