from flask import Blueprint, render_template, redirect, request, Response, jsonify, session, url_for, abort
from flask_login import login_required
from ...controllers.ControleLogin import ControleLogin
from ...controllers.ControleChave import ControleCrontoleDeChave
from ...extensions.Log import LogErro
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
        return render_template("controleChave/controleChave.html", context=context)
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
            return render_template("controleChave/incluirMovimentoChave.html", context=context)
        else:
            return redirect(url_for('controleChaveVigcBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para inserir a retirada da Chave
@controleChaveVigcBlue.route('/controle-chave/incluir-retirada', methods=["POST"])
@login_required
def insertRetirada():
    try:
        controleManterChave = ControleCrontoleDeChave()
        controleManterChave.inserirRetirada(request.form["dtRet"].strip(), request.form["hrRet"].strip(), request.form["chave"].strip())
        context = {"titulo": "Retirada de Chave", "active": "controlChav"}
        return render_template("controleChave/incluirMovimentoChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para vefrificar login do usuário
@controleChaveVigcBlue.route('/controle-chave/incluir-retirada/modal-login', methods=["POST"])
@login_required
def incluirRetiradaModalLogin():
    try:
        controleLogin = ControleLogin()
        dataJson = request.get_json()
        if dataJson["usuario"].upper().strip() == "VIG":
            resp = Response(response=json.dumps({"msg": "Este usuário não pode ser usado para está ação"}), status=500, mimetype="application/json")
            return resp
        else:
            respLogin = controleLogin.loginVig(dataJson["usuario"].upper().strip(), dataJson["senha"].upper().strip())  
            if respLogin == 4:
                resp = Response(response=json.dumps({"msg": "Usuário/Senha estão incorretos!"}), status=500, mimetype="application/json")
                return resp
            elif respLogin == 5:
                resp = Response(response=json.dumps({"msg": "Usuário está inativo ou deletado"}), status=500, mimetype="application/json")
                return resp
            elif respLogin == 6:
                resp = Response(response=json.dumps({"msg": "Usuário não existe"}), status=500, mimetype="application/json")
                return resp
            else:
                session["loginVig"] = True
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
        return render_template("controleChave/manutencaoChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)