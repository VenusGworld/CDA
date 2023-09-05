from flask import Blueprint, render_template, request, redirect, url_for, flash, abort, session
from ...controllers.ControleManterTerceiro import ControleManterTerceiro
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


terceiroVigBlue = Blueprint("terceiroVigBlue", __name__)

##############################################################
# Rotas relacionadas ao CRUD de Terceiro
##############################################################

#Rota para tela de listagem de terceiros
@terceiroVigBlue.route("/terceiro/lista-terceiros", methods=["GET"])
@login_required
def listaTerceiros():
    try:
        session["loginVig"] = False
        context = {"titulo": "Listagem de Terceiros", "active": "cadTerc"}
        return render_template("vigAdm/terceiro/listaTerceiros.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de cadastro de tereceiro
@terceiroVigBlue.route("/terceiro/cadastro-terceiro", methods=["GET"])
@login_required
def cadastroTerceiro():
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleManterFuncionario = ControleManterTerceiro()
            codigo = controleManterFuncionario.incrementaCodigoTerc()
            context = {"titulo": "Cadastro de Terceiro", "active": "cadTerc", "codigo": codigo}
            return render_template("vigAdm/terceiro/cadastroTerceiro.html", context=context)
        else:
            return redirect(url_for("chaveVigBlue.listaChaves"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de cadastro de tereceiro
@terceiroVigBlue.route("/terceiro/cadastro-terceiro", methods=["POST"])
@login_required
def insertTerceiro():
    try:
        controleManterFuncionario = ControleManterTerceiro()
        if controleManterFuncionario.incluirTerceiro(request.form["codigo"].upper().strip(), request.form["nome"].upper().strip(), request.form["cpf"]):
            flash("Terceiro incluido com sucesso!", "success")
            return redirect(url_for("terceiroVigBlue.listaTerceiros"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de edição da terceiro
@terceiroVigBlue.route("/terceiro/editar-terceiro-modal/<id>", methods=["GET"])
@login_required
def modalEditarTerceiro(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleManterFuncionario = ControleManterTerceiro()
            terceiro = controleManterFuncionario.consultaTerceiroDetalhadoId(int(id))
            context = {"titulo": "Listagem de Terceiros", "active": "cadTerc", "modal": 2, "terceiro": terceiro}
            return render_template("vigAdm/terceiro/listaTerceiros.html", context=context)
        else:
            return redirect(url_for("terceiroVigBlue.listaTerceiros"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para editar terceiro
@terceiroVigBlue.route("/terceiro/editar-terceiro", methods=["POST"])
@login_required
def editTerceiro():
    try:
        controleManterFuncionario = ControleManterTerceiro()
        if controleManterFuncionario.editarTerceiro(int(request.form["idTerc"]), request.form["codigoTerc"], request.form["cpfTerc"].upper().strip(), request.form["nomeTerc"].upper().strip(), request.form["observacaoEditar"].upper().strip()):
            flash("Terceiro alterado com sucesso!", "success")
            return redirect(url_for("terceiroVigBlue.listaTerceiros"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de confirmação de exclusão de terceiro
@terceiroVigBlue.route("/terceiro/excluir-terceiro-modal/<id>", methods=["GET"])
@login_required
def modalDeleteTerceiro(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleManterFuncionario = ControleManterTerceiro()
            terceiro = controleManterFuncionario.consultaTerceiroDetalhadoId(int(id))
            context = {"titulo": "Listagem de Terceiros", "active": "cadTerc", "modal": 1, "terceiro": terceiro}
            return render_template("vigAdm/terceiro/listaTerceiros.html", context=context)
        else:
            return redirect(url_for("terceiroVigBlue.listaTerceiros"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para exclusão da terceiro
@terceiroVigBlue.route("/terceiro/excluir-chave", methods=["POST"])
@login_required
def deleteTerceiro():
    try:
        controleManterFuncionario = ControleManterTerceiro()
        respControle = controleManterFuncionario.excluirTerceiro(int(request.form["idExcluir"]), request.form["observacaoExcluir"].upper().strip())
        if respControle == 1:
            flash("Terceiro excluido com sucesso!", "success")
        elif respControle == 2:
            flash("Terceiro possue movimentação no sistema, então foi desativado", "success")
        else:
            flash("Terceiro não pode ser excluido pois existe movimento(s) em aberto", "danger")
        
        return redirect(url_for("terceiroVigBlue.listaTerceiros"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)