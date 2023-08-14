from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, Response, abort, session
from ...controllers.ControleManterChave import ControleManterChave
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


chaveVigBlue = Blueprint("chaveVigBlue", __name__)

##############################################################
# Rotas relacionadas ao CRUD de Chaves
##############################################################

#Rota para a tela de listagem de chaves
@chaveVigBlue.route("/chave/lista-chaves", methods=["GET"])
@login_required
def listaChaves():
    try:
        session["loginVig"] = False
        context = {"titulo": "Listagem de Chaves", "active": "cadChave"}
        return render_template("vigAdm/chave/listaChaves.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de cadastro de chave
@chaveVigBlue.route("/chave/cadastro-chave", methods=["GET"])
@login_required
def cadastroChave():
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleManterChave = ControleManterChave()
            codigo = controleManterChave.incrementaCodigo()
            context = {"titulo": "Cadastro de Chaves", "active": "cadChave", "codigo": codigo}
            return render_template("vigAdm/chave/cadastroChave.html", context=context)
        else:
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inserir chave
@chaveVigBlue.route("/chave/cadastro-chave", methods=["POST"])
@login_required
def insertChave():
    try:
        controleManterChave = ControleManterChave()
        if controleManterChave.incluirChave(request.form["codigo"].upper().strip(), request.form["nome"].upper().strip()):
            flash("Chave incluida com sucesso!", "success")
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de edição da chave
@chaveVigBlue.route("/chave/editar-chave-modal/<id>", methods=["GET"])
@login_required
def modalEditarChave(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleManterChave = ControleManterChave()
            chave = controleManterChave.mostraChaveDetalhadaId(id)
            context = {"titulo": "Listagem de Chaves", "active": "cadChave", "modal": 2, "chave": chave}
            return render_template("vigAdm/chave/listaChaves.html", context=context)
        else:
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para editar chave
@chaveVigBlue.route("/chave/editar-chave", methods=["POST"])
@login_required
def editChave():
    try:
        controleManterChave = ControleManterChave()
        if controleManterChave.editarChave(int(request.form["idChav"]), request.form["codigoChav"], request.form["nomeChave"].upper().strip(), request.form["observacaoEditar"].upper().strip()):
            flash("Chave alterada com sucesso!", "success")
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de confirmação de exclusão da chave
@chaveVigBlue.route("/chave/excluir-chave-modal/<id>", methods=["GET"])
@login_required
def modalDeleteChave(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleManterChave = ControleManterChave()
            chave = controleManterChave.mostraChaveDetalhadaId(id)
            context = {"titulo": "Listagem de Chaves", "active": "cadChave", "modal": 1, "chave": chave}
            return render_template("vigAdm/chave/listaChaves.html", context=context)
        else:
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para exclusão da chave
@chaveVigBlue.route("/chave/excluir-chave", methods=["POST"])
@login_required
def deleteChave():
    try:
        controleManterChave = ControleManterChave()
        respControle = controleManterChave.excluirChave(int(request.form["idExcluir"]), request.form["observacaoExcluir"].upper().strip())
        if respControle == 1:
            flash("Chave excluida com sucesso!", "success")
            return redirect(url_for("chaveVigBlue.listaChaves"))
        elif respControle == 2:
            flash("Chave possue movimentação no sistema, então foi desativada", "success")
            return redirect(url_for("chaveVigBlue.listaChaves"))
        else:
            flash("Chave não pode ser excluida pois existe movimento em aberto", "danger")
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)