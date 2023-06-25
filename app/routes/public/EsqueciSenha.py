from flask import Blueprint, render_template, request, jsonify, Response, abort
from ...controllers.ControleEsqueciSenha import ControleEsqueciSenha
from ...extensions.Log import LogErro
import sys
import traceback
import json

esqueciSenhaBlue = Blueprint("esqueciSenhaBlue", __name__)

#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha-modal", methods=['GET'])
def modal():
    try:
        context = {"modal": 1} #Dcionário com as váriaveis parta utilizar no template
        return render_template("public/index.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha-modal", methods=['POST'])
def enviaDados():
    try:
        jsonData = request.get_json()
        controleEsqueciSenha = ControleEsqueciSenha()
        respControle = controleEsqueciSenha.verificarUsuario(jsonData["usuario"].upper().strip(), jsonData["email"].strip())
        if respControle == 1:
            resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
            return resp
        elif respControle == 2:
            resp = Response(response=json.dumps({"msg": "E-mail não enviado, contate a equipe de T.I"}), status=500, mimetype="application/json")
            return resp
        else:
            resp = Response(response=json.dumps({"msg": "E-mail/Usúario incorreto!"}), status=500, mimetype="application/json")
            return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha/<hash>", methods=['GET'])
def esquciSenhaHash(hash):
    try:
        controleEsqueciSenha = ControleEsqueciSenha()
        respControle = controleEsqueciSenha.verificarHash(hash)
        if respControle == 1:
            context = {"hash": hash}
            return render_template("public/novaSenha.html", context=context)
        else:
            pass
            #return render_template("error/404.html")
            
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha", methods=['POST'])
def esquciSenha():
    try:
        controleEsqueciSenha = ControleEsqueciSenha()
        jsonData = request.get_json()
        respControle = controleEsqueciSenha.trocaSenha(jsonData["senha"].upper().strip(), jsonData["hash"].upper())
        if respControle == 1:
            resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
            return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)