from flask import Blueprint, render_template, redirect, request, Response, jsonify, session, url_for, abort, flash
from ...controllers.ControleTerceiro import ControleTerceiro
from ...extensions.LogErro import LogErro
from flask_login import login_required
from datetime import datetime
import traceback
import json
import sys

controleTercVigBlue = Blueprint("controleTercVigBlue", __name__)


#Rota para a tela de controle de Treceiros
@controleTercVigBlue.route('/controle-terceiro', methods=["GET"])
@login_required
def controleTerceiro():
    try:
        session["loginVig"] = False
        context = {"titulo": "Contorle de Terceiros", "active": "controlTerc"}
        return render_template("vigAdm/controleTerceiro/controleTerceiro.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para a tela de incluir entrada de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-entrada', methods=["GET"])
@login_required
def incluirEntradaTerc():
    try:
        if session["loginVig"] or session["grupo"] == "ADM": #Verifica se o usuário está tentando acessar a pagina usando a URL
            data = datetime.now()
            context = {"titulo": "Entrada de Terceiro", "active": "controlTerc", "data": data}
            return render_template("vigAdm/controleTerceiro/incluirMovimentoTerceiro.html", context=context)
        else:
            return redirect(url_for('controleTercVigBlue.controleTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para incluir entrada de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-entrada', methods=["POST"])
@login_required
def insertEntradaTerc():
    try:
        dataJson = request.get_json()
        controleTerceiro = ControleTerceiro()
        controleTerceiro.inserirEntrada(dataJson["cpf"], dataJson["nome"], dataJson["empresa"], dataJson["placa"], dataJson["veiculo"], dataJson["motivo"], dataJson["pessoaVisit"], dataJson["dtEntrada"], dataJson["hrEntrada"], dataJson["acomps"])
        flash("Entrada de terceiro incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        resp = Response(response=json.dumps({"msg": "Error"}), status=500, mimetype="application/json")
        return resp
    

#Rota para modal de inclusão de saída de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-saida-modal/<id>', methods=["GET"])
@login_required
def incluirSaidaModalTerc(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleTerceiro = ControleTerceiro()
            movimento = controleTerceiro.consultaMovTercDetalhado(int(id))
            data = datetime.now()
            context = {"active": "controlTerc", "modal": 1, "movimento": movimento, "dataAtual": data}
            return render_template("vigAdm/controleTerceiro/controleTerceiro.html", context=context)
        else:
            return redirect(url_for('controleTercVigBlue.controleTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para inclusão de saída de terceiro
@controleTercVigBlue.route('/controle-terceiro/incluir-saida', methods=["POST"])
@login_required
def insertSaidaTerc():
    try:
        data = request.get_json()
        controleTerceiro = ControleTerceiro()
        controleTerceiro.inserirSaida(int(data["idMov"]), data["dataSaid"], data["horaSaid"], data["cpf"], data["acomps"], data["cracha"])
        flash("Saída incluida com sucesso!", "success")
        resp = Response(response=json.dumps({"success": True}), status=200, mimetype="application/json")
        return resp
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de manutenção de movimentação de terceiros
@controleTercVigBlue.route('/controle-terceiro/manutencao-terceiro', methods=["GET"])
@login_required
def manutencaoTerceiro():
    try:
        session["loginVig"] = False
        context = {"titulo": "Manutenção movimento de Terceiro", "active": "controlTerc"}
        return render_template("vigAdm/controleTerceiro/manutencaoTerceiro.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de edição dos dados do movimentos de terceiro
@controleTercVigBlue.route('/controle-terceiro/manutencao-terceiro/modal-visualizacao-controle-terceiro/<id>', methods=["GET"])
@login_required
def vizualizarMovimentoTerceiro(id):
    try:
        controleTerceiro = ControleTerceiro()
        movimento = controleTerceiro.consultaMovTercDetalhado(int(id))
        context = {"titulo": "Manutenção movimento de Terceiro", "active": "controlTerc", "modal": 1, "movimento": movimento}
        return render_template("vigAdm/controleTerceiro/manutencaoTerceiro.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de edição dos dados do movimentos de terceiro
@controleTercVigBlue.route('/controle-terceiro/manutencao-terceiro/editar-controle-terceiro/<id>', methods=["GET"])
@login_required
def editarMovimentoTerceiro(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleTerceiro = ControleTerceiro()
            movimento = controleTerceiro.consultaMovTercDetalhado(int(id))
            context = {"titulo": "Edição de Movimento de Terceiro", "active": "controlTerc", "movimento": movimento}
            return render_template("vigAdm/controleTerceiro/editarMovimentoTerceiro.html", context=context)
        else:
            return redirect(url_for('controleTercVigBlue.manutencaoTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para edição de movimento de terceiro
@controleTercVigBlue.route('/controle-terceiro/manutencao-terceiro/edicao-controle-terceiro', methods=["POST"])
@login_required
def editMovimentoTerceiro():
    try:
        controleTerceiro = ControleTerceiro()
        controleTerceiro.editarMovimentoTerceiro(request.form["idMov"], request.form["dataEnt"], request.form["horaEnt"], 
                                                request.form["dataSai"], request.form["horaSai"], request.form["crachaPessoaVisit"],
                                                request.form["observacaoEditar"].upper().strip())
        
        flash("Movimento alterado com sucesso!", "success")
        return redirect(url_for('controleTercVigBlue.manutencaoTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para modal de confirmação de exclusão do movimento de terceiro
@controleTercVigBlue.route('/controle-terceiro/manutencao-terceiro/modal-exclusão-controle-terceiro/<id>', methods=["GET"])
@login_required
def modalExcluirMovimentoTerceiro(id):
    try:
        if session["loginVig"] or session["grupo"] == "ADM":
            controleTerceiro = ControleTerceiro()
            movimento = controleTerceiro.consultaMovTercDetalhado(int(id))
            context = {"titulo": "Manutenção movimento de Terceiro", "active": "controlTerc", "modal": 2, "movimento": movimento}
            return render_template("vigAdm/controleTerceiro/manutencaoTerceiro.html", context=context)
        else:
            return redirect(url_for('controleTercVigBlue.manutencaoTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)



#Rota para exclusão do movimento de terceiro
@controleTercVigBlue.route('/controle-terceiro/manutencao-terceiro/exclusão-controle-terceiro', methods=["POST"])
@login_required
def excluirMovimentoTerceiro():
    try:
        controleTerceiro = ControleTerceiro()
        controleTerceiro.excluirMovimentoTerceiro(request.form["idExcluir"], request.form["crachaPessoaVisit"], request.form["observacaoExcluir"].upper().strip())
        flash("Movimento excluido com sucesso!", "success")
        return redirect(url_for('controleTercVigBlue.manutencaoTerceiro'))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)