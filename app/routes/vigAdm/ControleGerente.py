from flask import Blueprint, render_template, redirect, request, Response, session, url_for, abort, flash
from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleGerente import ControleDeGerente
from ...extensions.LogErro import LogErro
from flask_login import login_required
from datetime import datetime
import traceback
import sys
import json


controleGerVigBlue = Blueprint("controleGerVigBlue", __name__)


#Rota para a tela de controle de gerentes
@controleGerVigBlue.route('/controle-gerente', methods=["GET"])
@login_required
def controleGerente():
    try:
        session["loginVig"] = False
        context = {"titulo": "Contorle de Gerente", "active": "controlGer"}
        return render_template("vigAdm/controleGerente/controleGerente.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de incluir entrada do gerente
@controleGerVigBlue.route('/controle-gerente/incluir-entrada', methods=["GET"])
@login_required
def incluirEntradaGer():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Entrada de Gerente", "active": "controlGer", "data": data}
            return render_template("vigAdm/controleGerente/incluirMovimentoGerente.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleGerAdmBlue.controleGerente'))
            else:
                return redirect(url_for('controleGerVigBlue.controleGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para incluir a entrada de gerente
@controleGerVigBlue.route('/controle-gerente/incluir-entrada', methods=["POST"])
@login_required
def insertEntradaGer():
    try:
        controleGerente = ControleDeGerente()
        if controleGerente.inserirEntrada(request.form["dtEnt"], request.form["hrEnt"], request.form["gerente"]):
            flash("Entrada incluida com sucesso!", "success")
            if session["grupo"] == "ADM":
                return redirect(url_for('controleGerAdmBlue.controleGerente'))
            else:
                return redirect(url_for('controleGerVigBlue.controleGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de inclusão de saída de gerente
@controleGerVigBlue.route('/controle-gerente/incluir-saida-modal/<id>', methods=["GET"])
@login_required
def incluirSaidaGer(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleGerente = ControleDeGerente()
            movimento = controleGerente.consultaMovimentoDetalhado(id)
            data = datetime.now()
            context = {"active": "controlChav", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleGerente/controleGerente.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleGerAdmBlue.controleGerente'))
            else:
                return redirect(url_for('controleGerVigBlue.controleGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inclusão de saída de gerente
@controleGerVigBlue.route('/controle-gerente/incluir-saida', methods=["POST"])
@login_required
def insertSaidaGer():
    try:
        data = request.get_json()
        controleGerente = ControleDeGerente()
        controleGerente.inserirSaida(data["idMov"], data["dataSai"], data["horaSai"], data["crachaGer"])
        flash("Saída incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de manutenção de movimentação de gerentes
@controleGerVigBlue.route('/controle-gerente/manutencao-gerente', methods=["GET"])
@login_required
def manutencaoGerente():
    try:
        session["loginVig"] = False
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_MANUT_CONTROL_GER")
        context = {"titulo": "Manutenção movimento de Gerente", "active": "controlGer", "meses": meses}
        return render_template("vigAdm/controleGerente/manutencaoGerente.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de edição de movimento de gerentes
@controleGerVigBlue.route('/controle-gerente/manutencao-gerente/edicao-controle-gerente/<id>', methods=["GET"])
@login_required
def editarMovimentoGerente(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleGerente = ControleDeGerente()
            movimento = controleGerente.consultaMovimentoDetalhado(id)
            context = {"titulo": "Edição de Movimento de Gerente", "active": "controlGer", "movimento": movimento}
            return render_template("vigAdm/controleGerente/editarMovimentoGerente.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleGerAdmBlue.manutencaoGerente'))
            else:
                return redirect(url_for('controleGerVigBlue.manutencaoGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para edição de movimento de gerentes
@controleGerVigBlue.route('/controle-gerente/manutencao-gerente/edicao-controle-gerente', methods=["POST"])
@login_required
def editMovimentoGerente():
    try:
        controleGerente = ControleDeGerente()
        controleGerente.editarMovimentoGerente(request.form["idMov"], request.form["crachaGer"], request.form["dataEnt"], 
                                               request.form["horaEnt"], request.form["dataSai"], request.form["horaSai"],
                                               request.form["observacaoEditar"].upper().strip())
        
        flash("Movimento alterado com sucesso!", "success")
        if session["grupo"] == "ADM":
            return redirect(url_for('controleGerAdmBlue.manutencaoGerente'))
        else:
            return redirect(url_for('controleGerVigBlue.manutencaoGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de confirmação de exclusão do movimento de gerente
@controleGerVigBlue.route('/controle-gerente/manutencao-gerente/modal-exlusao-controle-gerente/<id>', methods=["GET"])
@login_required
def modalExclirMovimentoGerente(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleGerente = ControleDeGerente()
            movimento = controleGerente.consultaMovimentoDetalhado(id)
            context = {"titulo": "Manutenção movimento de Gerente", "active": "controlGer", "modal": 1, "movimento": movimento}
            return render_template("vigAdm/controleGerente/manutencaoGerente.html", context=context)
        else:
            if session["grupo"] == "ADM":
                return redirect(url_for('controleGerAdmBlue.manutencaoGerente'))
            else:
                return redirect(url_for('controleGerVigBlue.manutencaoGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para exclusão do movimento de gerente
@controleGerVigBlue.route('/controle-gerente/manutencao-gerente/modal-exlusao-controle-gerente', methods=["POST"])
@login_required
def exclirMovimentoGerente():
    try:
        controleGerente = ControleDeGerente()
        controleGerente.excluirMovimentoGerente(request.form["idExcluir"], request.form["crachaGer"], request.form["observacaoExcluir"])
        flash("Movimento excluido com sucesso!", "success")
        if session["grupo"] == "ADM":
            return redirect(url_for('controleGerAdmBlue.manutencaoGerente'))
        else:
            return redirect(url_for('controleGerVigBlue.manutencaoGerente'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)