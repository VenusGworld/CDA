from flask import Blueprint, render_template, request, Response, abort
from ...controllers.ControleEsqueciSenha import ControleEsqueciSenha
from ...extensions.LogErro import LogErro
import traceback
import sys
import json

esqueciSenhaBlue = Blueprint("esqueciSenhaBlue", __name__)

##############################################################
# Rotas relacionadas as funcionalidades da recuperação de senha
##############################################################

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
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para verificar os dados e enviar o e-mail com a informações para a alteração da senha
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
            resp = Response(response=json.dumps({"msg": "E-mail/Usúario incorreto!"}), status=401, mimetype="application/json")
            return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        resp = Response(response=json.dumps({"msg": "E-mail não enviado, contate a equipe de T.I"}), status=500, mimetype="application/json")
        return resp


#Rota para tela de alteração de senha
@esqueciSenhaBlue.route("/esqueci-senha/<hash>", methods=['GET'])
def esquciSenhaHash(hash):
    try:
        controleEsqueciSenha = ControleEsqueciSenha()
        respControle = controleEsqueciSenha.verificarHash(hash)
        if respControle == 1:
            context = {"hash": hash}
            return render_template("public/novaSenha.html", context=context)
        elif respControle == 3:
            return "<h1>Link expirado, solicite novamente!</h1>"
        else:
            return render_template("public/error/404.html"), 404
            
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para efetivar a alteração da senha
@esqueciSenhaBlue.route("/esqueci-senha", methods=['POST'])
def esquciSenha():
    try:
        controleEsqueciSenha = ControleEsqueciSenha()
        jsonData = request.get_json()
        controleEsqueciSenha.trocaSenha(jsonData["senha"].upper().strip(), jsonData["hash"].upper())
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        resp = Response(status=500, mimetype="application/json")
        return resp