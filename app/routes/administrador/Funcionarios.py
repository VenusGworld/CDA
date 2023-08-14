from flask import Blueprint, render_template, request, redirect, url_for, flash, Response, abort
from ...controllers.ControleManterFuncionario import ControleManterFuncionario
from ...extensions.Integracao import Integracao
from ...extensions.LogErro import LogErro
from flask_login import login_required
import distutils
import traceback
import json
import sys


funcionarioAdmBlue = Blueprint("funcionarioAdmBlue", __name__)

##############################################################
# Rotas relacionadas ao CRUD de Funcionários
##############################################################

#Rota para a tela de listagem de Funcionários
@funcionarioAdmBlue.route('/funcionario/lista-funcionarios', methods=["GET"])
@login_required
def listaFuncionariosAdm():
    try:
        context = {"titulo": "Listagem de Funcionários", "active": "cadFunc"}
        return render_template("administrador/funcionario/listaFuncionarios.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para o modal de confirmação de para a atualização de base
@funcionarioAdmBlue.route('/funcionario/lista-funcionarios-modal-integracao', methods=["GET"])
@login_required
def listaFuncionariosAdmModalIntegracao():
    try:
        context = {"titulo": "Listagem de Funcionários", "active": "cadFunc", "modal": 1}
        return render_template("administrador/funcionario/listaFuncionarios.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para atualizar a base de Funcionários
@funcionarioAdmBlue.route('/funcionario/atualiza-baseFunc', methods=["POST"])
@login_required
def atualizaBaseFunc():
    try:
        integracao = Integracao()
        integracao.integraFunc()
        flash("Base atualizada com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)
        

#Rota para a tela de cadastro de Funcionários
@funcionarioAdmBlue.route('/funcionario/cadastro-funcionario', methods=["GET"])
@login_required
def cadastroFuncionarioAdm():
    try:
        context = {"titulo": "Cadastro de Funcionário", "action": f"{url_for('funcionarioAdmBlue.insertFuncionarioAdm')}", "botao": "Cadastrar", "active": "cadFunc"}
        return render_template("administrador/funcionario/cadastroFuncionario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inserir Funcionários
@funcionarioAdmBlue.route('/funcionario/cadastro-funcionario', methods=["POST"])
@login_required
def insertFuncionarioAdm():
    try:
        controleManterFuncionario = ControleManterFuncionario()
        if controleManterFuncionario.incluirFuncionario(request.form["nome"].upper().strip(), request.form["cracha"].strip(), request.form["maquina"].upper().strip(), bool(distutils.util.strtobool(request.form["gerente"]))):
            flash("Funcionário incluido com sucesso!", "success")
            return redirect(url_for("funcionarioAdmBlue.listaFuncionariosAdm")) 
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela para editar o Funcionário
@funcionarioAdmBlue.route('/funcionario/editar-funcionario/<id>',  methods=["GET"])
@login_required
def editarFuncionarioAdm(id):
    try:
        controleManterFuncionario = ControleManterFuncionario()
        funcionario = controleManterFuncionario.mostraFuncionarioDetalhado(id)
        context = {"titulo": "Alterar Funcionário", "action": f"{url_for('funcionarioAdmBlue.editFuncionarioAdm')}", "botao": "Editar", "funcionario": funcionario, "active": "cadFunc"}
        return render_template("administrador/funcionario/cadastroFuncionario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para editar o Funcionário
@funcionarioAdmBlue.route('/funcionario/editar-funcionario',  methods=["POST"])
@login_required
def editFuncionarioAdm():
    try:
        controleManterFuncionario = ControleManterFuncionario()
        if controleManterFuncionario.editarFuncionario(request.form["id"], request.form["nome"].upper().strip(), request.form["cracha"].strip(), request.form["maquina"].upper().strip(), bool(distutils.util.strtobool(request.form["gerente"]))):
            flash("Funcionário alterado com sucesso!", "success")
            return redirect(url_for("funcionarioAdmBlue.listaFuncionariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a exclusão do Funcionário
@funcionarioAdmBlue.route('/funcionario/excluir-funcionario/<id>',  methods=["GET"])
@login_required
def deleteFuncionarioAdm(id):
    try: 
        controleManterFuncionario = ControleManterFuncionario()
        respControle = controleManterFuncionario.excluirFuncionario(int(id))
        if respControle == 1:
            flash("Funcionário excluido com sucesso!", "success")
            return redirect(url_for("funcionarioAdmBlue.listaFuncionariosAdm"))
        else:
            flash("Funcionário possue movimentação no sistema, então foi desativado", "success")
            return redirect(url_for("funcionarioAdmBlue.listaFuncionariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)
        