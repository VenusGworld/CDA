from flask import Blueprint, jsonify, session
from flask_login import login_required
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...controllers.ControleChave import ControleCrontoleDeChave
from ...controllers.ControleManterFuncionario import ControleManterFuncionario
from ...controllers.ControleManterChave import ControleManterChave
from ...controllers.ControleConsultarLogUser import ControleConsultarLogUser

preencheTabelasBlue = Blueprint("preencheTabelasBlue", __name__)

#Rota para preencher a lista de Usuários
@preencheTabelasBlue.route('/lista-usuarios', methods=["POST"])
@login_required
def listaUsuariosAPI():
    controleManterUsuario = ControleManterUsuario()
    respControle = controleManterUsuario.mostarUsuarios()
    return jsonify(respControle)


#Rotapara para preencher a lista de Chaves retiradas
@preencheTabelasBlue.route('/lista-chaves-retiradas', methods=["POST"])
@login_required
def listaChavesRetAPI():
    controleChave = ControleCrontoleDeChave()
    respControle = controleChave.listaChavesRetiradas()
    return jsonify({"login": session["grupo"]}, respControle)


#Rotapara para preencher a lista de Movimento de Chaves
@preencheTabelasBlue.route('/lista-chaves-manutencao', methods=["POST"])
@login_required
def listaChavesManutAPI():
    controleChave = ControleCrontoleDeChave()
    respControle = controleChave.listaChavesManut()
    return jsonify({"login": session["grupo"]}, respControle)


#Rota para preencher a lista de Funcionários
@preencheTabelasBlue.route('/lista-funcionarios', methods=["POST"])
@login_required
def listaFuncionariosAPI():
    controleManterFuncionario = ControleManterFuncionario()
    respControle = controleManterFuncionario.mostarFuncionarios()
    return jsonify(respControle)


#Rota para preencher a lista de Chaves
@preencheTabelasBlue.route('/lista-chaves', methods=["POST"])
@login_required
def listaChavesAPI():
    controleManterChave = ControleManterChave()
    respControle = controleManterChave.mostraChaves()
    return jsonify({"login": session["grupo"]}, respControle)


#Rota para preencher a lista de logs de usuários
@preencheTabelasBlue.route('/lista-logs-usuario-insert', methods=["POST"])
@login_required
def listaLogsUserInsertAPI():
    controleConsultaLogUser = ControleConsultarLogUser()
    respControle = controleConsultaLogUser.consultaLogUserInsert()
    return jsonify(respControle)


#Rota para preencher a lista de logs de usuários
@preencheTabelasBlue.route('/lista-logs-usuario-update', methods=["POST"])
@login_required
def listaLogsUserUpdateAPI():
    controleConsultaLogUser = ControleConsultarLogUser()
    respControle = controleConsultaLogUser.consultaLogUserUpdate()
    return jsonify(respControle)


#Rota para preencher a lista de logs de usuários
@preencheTabelasBlue.route('/lista-logs-usuario-delete', methods=["POST"])
@login_required
def listaLogsUserDeleteAPI():
    controleConsultaLogUser = ControleConsultarLogUser()
    respControle = controleConsultaLogUser.consultaLogUserDelete()
    return jsonify(respControle)