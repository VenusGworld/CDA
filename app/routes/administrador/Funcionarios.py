from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, Response, abort
from flask_login import login_required
from ...controllers.ControleManterFuncionario import ControleManterFuncionario
from ...extensions.Integracao import Integracao
from ...extensions.Log import LogErro
import json
import sys
import distutils
import traceback

funcionarioAdmBlue = Blueprint("funcionarioAdmBlue", __name__)


#Rota para a tela de listagem de Funcionarios
@funcionarioAdmBlue.route('/lista-funcionarios', methods=["GET"])
@login_required
def listaFuncionariosAdm():
    try:
        context = {"titulo": "Listagem de Funcionários", "active": "cadFunc"}
        return render_template("administrador/funcionario/listaFuncionarios.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela de listagem de Funcionários com modal de confirmação de para a atualização de base
@funcionarioAdmBlue.route('/lista-funcionarios-modal-integracao', methods=["GET"])
@login_required
def listaFuncionariosAdmModalIntegracao():
    try:
        context = {"titulo": "Listagem de Funcionários", "active": "cadFunc", "modal": 1}
        return render_template("administrador/funcionario/listaFuncionarios.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para atualizar a base de Funcionários
@funcionarioAdmBlue.route('/atualiza-baseFunc', methods=["POST"])
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
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)
        

#Rota para a tela de listagem de Funcionarios
@funcionarioAdmBlue.route('/cadastro-funcionario', methods=["GET"])
@login_required
def cadastroFuncionarioAdm():
    try:
        context = {"titulo": "Cadastro de Funcionário", "action": f"{url_for('funcionarioAdmBlue.insertFuncionarioAdm')}", "botao": "Cadastrar", "active": "cadFunc"}
        return render_template("administrador/funcionario/cadastroFuncionario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela de listagem de Funcionarios
@funcionarioAdmBlue.route('/cadastro-funcionario', methods=["POST"])
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
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela para editar o Funcionário
@funcionarioAdmBlue.route('/editar-funcionario/<id>',  methods=["GET"])
@login_required
def editarFuncionarioAdm(id):
    try:
        controleManterUsuario = ControleManterFuncionario()
        funcionario = controleManterUsuario.mostraFuncionarioDetalhado(id)
        context = {"titulo": "Alterar Funcionário", "action": f"{url_for('funcionarioAdmBlue.editFuncionarioAdm')}", "botao": "Editar", "funcionario": funcionario, "active": "cadFunc"}
        return render_template("administrador/funcionario/cadastroFuncionario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela para editar o Funcionário
@funcionarioAdmBlue.route('/editar-funcionario',  methods=["POST"])
@login_required
def editFuncionarioAdm():
    try:
        controleManterUsuario = ControleManterFuncionario()
        if controleManterUsuario.editarFuncionario(request.form["id"], request.form["nome"].upper().strip(), request.form["cracha"].strip(), request.form["maquina"].upper().strip(), bool(distutils.util.strtobool(request.form["gerente"]))):
            flash("Funcionário alterado com sucesso!", "success")
            return redirect(url_for("funcionarioAdmBlue.listaFuncionariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)