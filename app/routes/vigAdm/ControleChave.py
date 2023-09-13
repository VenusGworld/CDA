from flask import Blueprint, render_template, redirect, request, Response, session, url_for, abort, flash
from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleChave import ControleChave
from ...extensions.LogErro import LogErro
from flask_login import login_required
from datetime import datetime
import traceback
import json
import sys


controleChaveVigBlue = Blueprint("controleChaveVigBlue", __name__)


#Rota para a tela de controle de Chaves
@controleChaveVigBlue.route('/controle-chave', methods=["GET"])
@login_required
def controleChave():
    try:
        session["loginVig"] = False
        context = {"titulo": "Contorle de Chaves", "active": "controlChav"}
        return render_template("vigAdm/controleChave/controleChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de incluir retirada da Chave
@controleChaveVigBlue.route('/controle-chave/incluir-retirada', methods=["GET"])
@login_required
def incluirRetiradaChav():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Retirada de Chave", "active": "controlChav", "data": data}
            return render_template("vigAdm/controleChave/incluirMovimentoChave.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleChaveAdmBlue.controleChave'))
            else:
                return redirect(url_for('controleChaveVigBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para incluir a reirada da chave
@controleChaveVigBlue.route('/controle-chave/incluir-retirada', methods=["POST"])
@login_required
def insertRetiradaChav():
    try:
        controleChave = ControleChave()
        if controleChave.inserirRetirada(request.form["dtRet"], request.form["hrRet"], request.form["chave"], request.form["responsavel"]):
            flash("Retirada incluida com sucesso!", "success")
            if session["grupo"] == "ADM":
                return redirect(url_for('controleChaveAdmBlue.controleChave'))
            else:
                return redirect(url_for('controleChaveVigBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de inclusão de devolução
@controleChaveVigBlue.route('/controle-chave/incluir-devolucao-modal/<id>', methods=["GET"])
@login_required
def incluirDevolucaoChav(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleChave = ControleChave()
            movimento = controleChave.consultaMovimentoDetalhado(id)
            data = datetime.now()
            context = {"active": "controlChav", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleChave/controleChave.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleChaveAdmBlue.controleChave'))
            else:
                return redirect(url_for('controleChaveVigBlue.controleChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inscluir a devolução de uma chave
@controleChaveVigBlue.route('/controle-chave/incluir-devolucao', methods=["POST"])
@login_required
def insertDevolucaoChav():
    try:
        data = request.get_json()
        controleChave = ControleChave()
        controleChave.inserirDevolucao(data["idMov"], data["dataDev"], data["horaDev"], data["respDev"], data["check"])
        flash("Devolução incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de manutenção da chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave', methods=["GET"])
@login_required
def manutencaoChave():
    try:
        session["loginVig"] = False
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_MANUT_CONTROL_CHAV")
        context = {"titulo": "Manutenção movimento de Chave", "active": "controlChav", "meses": meses}
        return render_template("vigAdm/controleChave/manutencaoChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de edição dos dados do movimentos de chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave/modal-visualizacao-controle-chave/<id>', methods=["GET"])
@login_required
def vizualizarMovimentoChave(id):
    try:
        controleChave = ControleChave()
        movimento = controleChave.consultaMovimentoDetalhado(id)
        context = {"titulo": "Manutenção movimento de Chave", "active": "controlChav", "modal": 1, "movimento": movimento}
        return render_template("vigAdm/controleChave/manutencaoChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de exibição dos dados da controle de chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave/edicao-controle-chave/<id>', methods=["GET"])
@login_required
def editarMovimentoChave(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleChave = ControleChave()
            movimento = controleChave.consultaMovimentoDetalhado(id)
            context = {"titulo": "Edição de Movimento de Chave", "active": "controlChav", "movimento": movimento}
            return render_template("vigAdm/controleChave/editarmovimentoChave.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleChaveAdmBlue.manutencaoChave'))
            else:
                return redirect(url_for('controleChaveVigBlue.manutencaoChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de confirmção de exclusão de movimento de chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave/edicao-controle-chave', methods=["POST"])
@login_required
def editMovimentoChave():
    try:
        controleChave = ControleChave()
        controleChave.editarMovimentoChave(request.form["idMov"], request.form["dataRet"], request.form["horaRet"], request.form["crachaRet"],
                                           request.form["dataDev"], request.form["horaDev"], request.form["crachaDev"], request.form["codigoChave"], 
                                           request.form["observacaoEditar"].upper().strip())
        
        flash("Movimento alterado com sucesso!", "success")
        if session["grupo"] == "ADM":
            return redirect(url_for('controleChaveAdmBlue.manutencaoChave'))
        else:
            return redirect(url_for('controleChaveVigBlue.manutencaoChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de exibição dos dados da controle de chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave/modal-exlusao-controle-chave/<id>', methods=["GET"])
@login_required
def modalExclirMovimentoChave(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleChave = ControleChave()
            movimento = controleChave.consultaMovimentoDetalhado(id)
            context = {"titulo": "Manutenção movimento de Chave", "active": "controlChav", "modal": 2, "movimento": movimento}
            return render_template("vigAdm/controleChave/manutencaoChave.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleChaveAdmBlue.manutencaoChave'))
            else:
                return redirect(url_for('controleChaveVigBlue.manutencaoChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de exibição dos dados da controle de chave
@controleChaveVigBlue.route('/controle-chave/manutencao-chave/exlusao-controle-chave', methods=["POST"])
@login_required
def excluirMovimentoChave():
    try:
        controleChave = ControleChave()
        controleChave.excluirMovimentoChave(request.form["idExcluir"], request.form["observacaoExcluir"].upper().strip())
        flash("Movimento excluido com sucesso!", "success")
        if session["grupo"] == "ADM":
            return redirect(url_for('controleChaveAdmBlue.manutencaoChave'))
        else:
            return redirect(url_for('controleChaveVigBlue.manutencaoChave'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)