from ...controllers.ControleManterFuncionario import ControleManterFuncionario
from ...controllers.ControleConsultarLogUser import ControleConsultarLogUser
from ...controllers.ControleManterTerceiro import ControleManterTerceiro
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...controllers.ControleManterChave import ControleManterChave
from flask import Blueprint, jsonify, session, request, Response
from ...controllers.ControleTerceiro import ControleTerceiro
from ...controllers.ControleGerente import ControleDeGerente
from ...controllers.ControleChave import CrontoleDeChave
from flask_login import login_required
import json

preencheTabelasBlue = Blueprint("preencheTabelasBlue", __name__)

##############################################################
# Rotas relacionadas ao preenchimento de tabelas
##############################################################

#Rota para preencher a lista de Usuários
@preencheTabelasBlue.route('/lista-usuarios', methods=["POST"])
@login_required
def listaUsuariosAPI():
    controleManterUsuario = ControleManterUsuario()
    respControle = controleManterUsuario.mostarUsuarios()
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rotapara para preencher a lista de Chaves retiradas
@preencheTabelasBlue.route('/lista-chaves-retiradas', methods=["POST"])
@login_required
def listaChavesRetAPI():
    controleChave = CrontoleDeChave()
    respControle = controleChave.listaChavesRetiradas()
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rotapara para preencher a lista de Movimento de Chaves
@preencheTabelasBlue.route('/lista-chaves-manutencao', methods=["POST"])
@login_required
def listaChavesManutAPI():
    controleChave = CrontoleDeChave()
    respControle = controleChave.listaChavesManut()
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Funcionários
@preencheTabelasBlue.route('/lista-funcionarios', methods=["POST"])
@login_required
def listaFuncionariosAPI():
    controleManterFuncionario = ControleManterFuncionario()
    respControle = controleManterFuncionario.mostarFuncionarios()
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Chaves
@preencheTabelasBlue.route('/lista-chaves', methods=["POST"])
@login_required
def listaChavesAPI():
    controleManterChave = ControleManterChave()
    respControle = controleManterChave.mostraChaves()
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de usuários
@preencheTabelasBlue.route('/lista-logs-usuario', methods=["POST"])
@login_required
def listaLogsUserInsertAPI():
    data = request.get_json()
    controleConsultaLogUser = ControleConsultarLogUser()
    if data["tipo"] == "INSERT":
        respControle = controleConsultaLogUser.consultaLogUserInsert()
    elif data["tipo"] == "UPDATE":
        respControle = controleConsultaLogUser.consultaLogUserUpdate()
    elif data["tipo"] == "ACTIVE":
        respControle = controleConsultaLogUser.consultaLogUserActive()
    else:
        respControle = controleConsultaLogUser.consultaLogUserDelete()
    
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp
    

#Rota para preencher a lista de Terceiros
@preencheTabelasBlue.route('/lista-terceiros', methods=["POST"])
@login_required
def listaTerceirosAPI():
    controleManterTerceiro = ControleManterTerceiro()
    respControle = controleManterTerceiro.mostrarTerceiros()
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Terceiros que entraram
@preencheTabelasBlue.route('/lista-terceiros-entradas', methods=["POST"])
@login_required
def listaTerceirosEntradaAPI():
    controleTerceiro = ControleTerceiro()
    respControle = controleTerceiro.consultaTerceirosEntrada()
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Terceiros que entraram
@preencheTabelasBlue.route('/lista-gerentes-entradas', methods=["POST"])
@login_required
def listaGerestesEntradaAPI():
    controlegerente = ControleDeGerente()
    respControle = controlegerente.consultaGerentesEntrada()
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp