from flask import Blueprint, request, redirect, session, flash, url_for, abort, Response
from flask_login import login_required
from ...models.Tables import *
from ...controllers.ControleLogin import ControleLogin
from ...extensions.LogErro import LogErro
import sys
import traceback
import json

autenticacaoBlue = Blueprint('autenticacaoBlue', __name__)


#Rota para efetuar o login no sistema
@autenticacaoBlue.route('/login', methods=['POST'])
def login():
    try:
        controleLogin = ControleLogin()
        respLogin = controleLogin.login(request.form["user"].upper().strip(), request.form["pssd"].upper().strip())
        if respLogin == 1: #Redireciona para o acesso de administrador
            session.permanent = True
            return redirect(url_for("dashAdmBlue.dashboard"))
        elif respLogin == 2: #Redireciona para o acesso de tecnico de segurança
            session.permanent = True
            return redirect(url_for("dashTecBlue.dashboardTec"))
        elif respLogin == 3: #Redireciona para o acesso de vigilante
            session.permanent = True
            return redirect(url_for("dashVigBlue.dashboard"))
        elif respLogin == 4:
            flash("Usuário/Senha incorreto!")
            return redirect("/index")
        elif respLogin == 5:
            flash("Usuário inativo ou deletado")
            return redirect("/index")
        else:
            flash("Usuário não existe")
            return redirect("/index")
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para verificar login de movimentação no sistema
@autenticacaoBlue.route('/modal-login', methods=["POST"])
@login_required
def incluirRetiradaModalLogin():
    try:
        controleLogin = ControleLogin()
        dataJson = request.get_json()
        if dataJson["usuario"].upper().strip() == "VIG":
            resp = Response(response=json.dumps({"msg": "Este usuário não pode ser usado para está ação"}), status=403, mimetype="application/json")
            return resp
        else:
            respLogin = controleLogin.loginVig(dataJson["usuario"].upper().strip(), dataJson["senha"].upper().strip())  
            if respLogin == 4:
                resp = Response(response=json.dumps({"msg": "Usuário/Senha estão incorretos!"}), status=401, mimetype="application/json")
                return resp
            elif respLogin == 5:
                resp = Response(response=json.dumps({"msg": "Usuário está inativo ou deletado"}), status=403, mimetype="application/json")
                return resp
            elif respLogin == 6:
                resp = Response(response=json.dumps({"msg": "Usuário não existe"}), status=404, mimetype="application/json")
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


#Rota para efetuar logout no sistema
@autenticacaoBlue.route('/logout', methods=['GET'])
@login_required
def logout():
    controleLogin = ControleLogin()
    controleLogin.logout()
    return redirect("/")
