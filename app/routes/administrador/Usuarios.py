from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


usuarioAdmBlue = Blueprint("usuarioAdmBlue", __name__)

##############################################################
# Rotas relacionadas ao CRUD de Usuários
##############################################################

#Rota para a tela de listagem de usuários
@usuarioAdmBlue.route('/usuario/lista-usuarios', methods=["GET"])
@login_required
def listaUsuariosAdm():
    try:
        context = {"titulo": "Listagem de Usuários", "active": "cadUser"}
        return render_template("administrador/usuario/listaUsuarios.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de cadastro de usuários
@usuarioAdmBlue.route('/usuario/cadastro-usuario', methods=["GET"])
@login_required
def cadastroUsuarioAdm():
    try:
        context = {"titulo": "Cadastro de Usuário", "action": f"{url_for('usuarioAdmBlue.insertUsuarioAdm')}", "botao": "Cadastrar", "active": "cadUser"}
        return render_template("administrador/usuario/cadastroUsuario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inserir usuário
@usuarioAdmBlue.route('/usuario/cadastro-usuario',  methods=["POST"])
@login_required
def insertUsuarioAdm():
    try:
        controleManterUsuario = ControleManterUsuario()
        if controleManterUsuario.incluirUsuario(request.form["nome"].upper().strip(), request.form["usuario"].upper().strip(), request.form["email"].strip(), request.form["grupo"], request.form["senha"].upper().strip()):
            flash("Usuário incluido com sucesso!", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))         
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela para editar o usuário
@usuarioAdmBlue.route('/usuario/editar-usuario/<id>',  methods=["GET"])
@login_required
def editarUsuarioAdm(id):
    try:
        controleManterUsuario = ControleManterUsuario()
        usuario = controleManterUsuario.consultarUsuarioDetalhado(id)
        context = {"titulo": "Alterar Usuário", "action": f"{url_for('usuarioAdmBlue.editUsuarioAdm')}", "botao": "Editar", "usuario": usuario, "active": "cadUser"}
        return render_template("administrador/usuario/cadastroUsuario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para editar o usuário
@usuarioAdmBlue.route('/usuario/editar-usuario',  methods=["POST"])
@login_required
def editUsuarioAdm():
    try:
        controleManterUsuario = ControleManterUsuario()
        if controleManterUsuario.editarUsuario(request.form["id"], request.form["nome"].upper().strip(), request.form["usuario"].upper().strip(), request.form["email"].strip(), request.form["grupo"], request.form["senha"].strip().strip()):
            flash("Usuário alterado com sucesso!", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)
    

#Rota para exclusão de usuário
@usuarioAdmBlue.route('/usuario/excluir-usuario/<id>',  methods=["GET"])
@login_required
def deleteUsuarioAdm(id):
    try: 
        controleManterUsuario = ControleManterUsuario()
        respControle = controleManterUsuario.excluirUsuario(int(id))
        if respControle == 1:
            flash("Usuário logado não pode ser excluido", "danger")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
        elif respControle == 2:
            flash("Usuário excluido com sucesso!", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
        else:
            flash("Usuário possue movimentação no sistema, então foi desativado", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)
        
