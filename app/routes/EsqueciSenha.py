from flask import Blueprint, render_template, request, jsonify, Response
from ..controllers.ControleEsqueciSenha import ControleEsqueciSenha
import json

esqueciSenhaBlue = Blueprint("esqueciSenhaBlue", __name__)

#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha-modal", methods=['GET'])
def modal():
    context = {"modal": 1} #Dcionário com as váriaveis parta utilizar no template
    return render_template("index.html", context=context)


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha-modal", methods=['POST'])
def enviaDados():
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


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha/<hash>", methods=['GET'])
def esquciSenhaHash(hash):
    controleEsqueciSenha = ControleEsqueciSenha()
    respControle = controleEsqueciSenha.verificarHash(hash)
    if respControle == 1:
        context = {"hash": hash}
        return render_template("novaSenha.html", context=context)
    else:
        return render_template("404.html")


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@esqueciSenhaBlue.route("/esqueci-senha", methods=['POST'])
def esquciSenha():
    controleEsqueciSenha = ControleEsqueciSenha()
    jsonData = request.get_json()
    respControle = controleEsqueciSenha.trocaSenha(jsonData["senha"].upper().strip(), jsonData["hash"].upper())
    if respControle == 1:
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp