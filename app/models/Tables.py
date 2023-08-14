from sqlalchemy import Column, LargeBinary, Integer, String, Boolean, DateTime
from ..configurations.Database import DB
from flask_login import UserMixin
from datetime import datetime

'''
@author Fabio
@version 4.0
@since 27/06/2023
'''

#Tabela de Usuários
class SysUser(UserMixin, DB.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    us_nome = Column(String(45), nullable=False)
    us_email = Column(String(80), nullable=False)
    us_usuario = Column(String(10),  nullable=False, unique=True)
    us_senha = Column(String(65),  nullable=False)
    us_grupo = Column(String(5),  nullable=False)
    us_complex = Column(String(36), nullable=False)
    us_hashNovaSenha = Column(String(10), nullable=False)
    us_novaSenha = Column(Boolean, nullable=False)
    us_limiteNovasenha = Column(String(30), nullable=False)
    us_ativo = Column(Boolean, nullable=False)
    us_delete = Column(Boolean, nullable=False)
    
    def __init__(self, nome: str, email: str, usuario: str, senha: str, grupo: str, complex: str, hashNovaSenha: str, senhaNova: bool, limiteNovaSenha, ativo: bool, delete: bool):
        #Função para instanciar um objeto para adcionar no banco
        self.us_nome = nome
        self.us_email = email
        self.us_usuario = usuario
        self.us_senha = senha
        self.us_grupo = grupo
        self.us_complex = complex
        self.us_hashNovaSenha = hashNovaSenha
        self.us_novaSenha = senhaNova
        self.us_limiteNovasenha = limiteNovaSenha
        self.us_ativo = ativo
        self.us_delete = delete


#Tabela de Chaves
class CDA005(DB.Model):
    id_chave = Column(Integer, primary_key=True, nullable=False)
    ch_codigo = Column(String(6), nullable=False)
    ch_nome = Column(String(30), nullable=False)
    ch_ativo = Column(Boolean, nullable=False)
    ch_delete = Column(Boolean, nullable=False)

    def __init__(self, codigo: str, nome: str, ativo: bool, delete: bool):
        #Função para instanciar um objeto para adcionar no banco
        self.ch_codigo = codigo
        self.ch_nome = nome
        self.ch_ativo = ativo
        self.ch_delete = delete


#Tabela de Movimento Chave
class CDA002(DB.Model):
    id_movChave = Column(Integer, primary_key=True, nullable=False)
    mch_dataRet = Column(String(8), nullable=False)
    mch_horaRet = Column(String(5), nullable=False)
    mch_respRet = Column(Integer, nullable=False)
    mch_dataDev = Column(String(8))
    mch_horaDev = Column(String(5))
    mch_respDev = Column(Integer)
    mch_delete = Column(Boolean, nullable=False)
    mch_idChav = Column(Integer, nullable=False)

    def __init__(self, dataRet: str, horaRet: str, delete: bool, idChave: int, idFunc: int):
        #Função para instanciar um objeto para adcionar no banco
        self.mch_dataRet = dataRet
        self.mch_horaRet = horaRet
        self.mch_delete = delete
        self.mch_respRet = idFunc
        self.mch_idChav = idChave


#Tabela de Log Movimento Chave
class CDA001(DB.Model):
    id_logChave = Column(Integer, primary_key=True, nullable=False)
    lmch_dataHora = Column(DateTime, nullable=False)
    lmch_acao = Column(String(45), nullable=False)
    lmch_observacao = Column(String(120), nullable=False)
    lmch_dadosAntigos = Column(LargeBinary)
    lmch_dadosNovos = Column(LargeBinary)
    lmch_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, observacao: str, idUsua: int, dadosAntigos: bytes, dadosNovos: bytes):
        #Função para instanciar um objeto para adcionar no banco
        self.lmch_dataHora = dataHora
        self.lmch_acao = acao
        self.lmch_observacao = observacao
        self.lmch_dadosAntigos = dadosAntigos
        self.lmch_dadosNovos = dadosNovos
        self.lmch_idUsua = idUsua


#Tabela de Funcionarios
class CDA007(DB.Model):
    id_funcionarios = Column(Integer, primary_key=True, nullable=False)
    fu_cracha = Column(String(6), nullable=False)
    fu_nome = Column(String(45), nullable=False)
    fu_maquina = Column(String(20))
    fu_gerente = Column(Boolean)
    fu_ativo = Column(Boolean, nullable=False)
    fu_delete = Column(Boolean, nullable=False)

    def __init__(self, cracha: str, nome: str, ativo: bool, delete: bool, gerente: bool, maquina: str):
        #Função para instanciar um objeto para adcionar no banco
        self.fu_cracha = cracha
        self.fu_nome = nome
        self.fu_maquina = maquina
        self.fu_gerente = gerente
        self.fu_ativo = ativo
        self.fu_delete = delete
    

#Tabela de Movimento Gerente
class CDA003(DB.Model):
    id_movGere = Column(Integer, primary_key=True, nullable=False)
    mge_dataEntra = Column(String(8),  nullable=False)
    mge_horaEntra = Column(String(5), nullable=False)
    mge_dataSaid = Column(String(8))
    mge_horaSaid = Column(String(5))
    mge_delete = Column(Boolean, nullable=False)
    mge_idFunc = Column(Integer, nullable=False)

    def __init__(self, dataEntrada: str, horaEntrada: str, delete: bool, idFunc: int):
        #Função para instanciar um objeto para adcionar no banco
        self.mge_dataEntra = dataEntrada
        self.mge_horaEntra = horaEntrada
        self.mge_delete = delete
        self.mge_idFunc = idFunc
    

#Tabela de Log Movimento Gerente
class CDA006(DB.Model):
    id_logGere = Column(Integer, primary_key=True, nullable=False)
    lmge_dataHora = Column(DateTime, nullable=False)
    lmge_acao = Column(String(45), nullable=False)
    lmge_observacao = Column(String(120), nullable=False)
    lmge_dadosAntigos = Column(LargeBinary)
    lmge_dadosNovos = Column(LargeBinary)
    lmge_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, observacao: str, dadosAntigos: bytes, dadosNovos: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lmge_dataHora = dataHora
        self.lmge_acao = acao
        self.lmge_observacao = observacao
        self.lmge_dadosAntigos = dadosAntigos
        self.lmge_dadosNovos = dadosNovos
        self.lmge_idUsua = idUsua


#Tabela de Terceiro
class CDA009(DB.Model):
    id_terceiro = Column(Integer, primary_key=True, nullable=False)
    te_codigo = Column(String(6), nullable=False)
    te_nome = Column(String(45), nullable=False)
    te_cpf = Column(String(11), nullable=False)
    te_ativo = Column(Boolean, nullable=False)
    te_delete = Column(Boolean, nullable=False)

    def __init__(self, codigo: str, nome: str, cpf: str, ativo: bool, delete: bool):
        #Função para instanciar um objeto para adcionar no banco
        self.te_codigo = codigo
        self.te_nome = nome
        self.te_cpf = cpf
        self.te_ativo = ativo
        self.te_delete = delete


#Tabela de Movimento de Terceiro
class CDA004(DB.Model):
    id_movTerc = Column(Integer, primary_key=True, nullable=False)
    mte_dataEntra = Column(String(8), nullable=False)
    mte_horaEntra = Column(String(5), nullable=False)
    mte_empresa = Column(String(45))
    mte_veiculo = Column(String(45))
    mte_placa = Column(String(10))
    mte_motivo = Column(String(45), nullable=False)
    mte_dataSaid = Column(String(8))
    mte_horaSaid = Column(String(5))
    mte_delete = Column(Boolean, nullable=False)
    mte_idFunc = Column(Integer, nullable=False)

    def __init__(self, dataEntrada: str, horaEntrada: str, empresa: str, veiculo: str, placa: str, motivo: str, detele: bool, idFunc: int):
        #Função para instanciar um objeto para adcionar no banco
        self.mte_dataEntra = dataEntrada
        self.mte_horaEntra = horaEntrada
        self.mte_empresa = empresa
        self.mte_veiculo = veiculo
        self.mte_placa = placa
        self.mte_motivo = motivo
        self.mte_delete = detele
        self.mte_idFunc = idFunc


#Tabela de Log Movimento de Terceiro
class CDA008(DB.Model):
    id_logTerc = Column(Integer, primary_key=True, nullable=False)
    lmte_dataHora = Column(DateTime, nullable=False)
    lmte_acao = Column(String(45), nullable=False)
    lmte_observacao = Column(String(120), nullable=False)
    lmte_dadosAntigos = Column(LargeBinary)
    lmte_dadosNovos = Column(LargeBinary)
    lmte_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, observacao: str, dadosAntigos: bytes, dadosNovos: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lmte_dataHora = dataHora
        self.lmte_acao = acao
        self.lmte_observacao = observacao
        self.lmte_dadosAntigos = dadosAntigos
        self.lmte_dadosNovos = dadosNovos
        self.lmte_idUsua = idUsua

    
#Tabela de Log Chave
class CDA010(DB.Model):
    id_logChave = Column(Integer, primary_key=True, nullable=False)
    lch_dataHora = Column(DateTime, nullable=False)
    lch_acao = Column(String(45), nullable=False)
    lch_observacao = Column(String(120), nullable=False)
    lch_dadosAntigos = Column(LargeBinary)
    lch_dadosNovos = Column(LargeBinary)
    lch_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, observacao: str, dadosAntigos: bytes, dadosNovos: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lch_dataHora = dataHora
        self.lch_acao = acao
        self.lch_observacao = observacao
        self.lch_dadosAntigos = dadosAntigos
        self.lch_dadosNovos = dadosNovos
        self.lch_idUsua = idUsua


#Tabela de Log Funcionarios
class CDA011(DB.Model):
    id_logFunc = Column(Integer, primary_key=True, nullable=False)
    lfu_dataHora = Column(DateTime, nullable=False)
    lfu_acao = Column(String(45), nullable=False)
    lfu_dadosAntigos = Column(LargeBinary)
    lfu_dadosNovos = Column(LargeBinary)
    lfu_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, dadosAntigos: bytes, dadosNovos: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lfu_dataHora = dataHora
        self.lfu_acao = acao
        self.lfu_dadosAntigos = dadosAntigos
        self.lfu_dadosNovos = dadosNovos
        self.lfu_idUsua = idUsua


#Tabela de Log Terceiro
class CDA012(DB.Model):
    id_logTerc = Column(Integer, primary_key=True, nullable=False)
    lte_dataHora = Column(DateTime, nullable=False)
    lte_acao = Column(String(45), nullable=False)
    lte_observacao = Column(String(120), nullable=False)
    lte_dadosAntigos = Column(LargeBinary)
    lte_dadosNovos = Column(LargeBinary)
    lte_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, observacao: str, dadosAntigos: bytes, dadosNovos: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lte_dataHora = dataHora
        self.lte_acao = acao
        self.lte_observacao = observacao
        self.lte_dadosAntigos = dadosAntigos
        self.lte_dadosNovos = dadosNovos
        self.lte_idUsua = idUsua


#Tabela de Log Usuário
class CDA013(DB.Model):
    id_logUsua = Column(Integer, primary_key=True, nullable=False)
    lus_dataHora = Column(DateTime, nullable=False)
    lus_acao = Column(String(45), nullable=False)
    lus_dadosAntigos = Column(LargeBinary)
    lus_dadosNovos = Column(LargeBinary)
    lus_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, dadosAntigos: bytes, dadosNovos: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lus_dataHora = dataHora
        self.lus_acao = acao
        self.lus_dadosAntigos = dadosAntigos
        self.lus_dadosNovos = dadosNovos
        self.lus_idUsua = idUsua


#Tabela de Log Mensagem
class CDA014(DB.Model):
    id_logMens = Column(Integer, primary_key=True, nullable=False)
    lme_dataHora = Column(DateTime, nullable=False)
    lme_mensagem = Column(LargeBinary)
    lme_idUsua = Column(Integer, nullable=False)

    def __init__(self, dataHora: datetime, acao: str, mensagem: bytes, idUsua: int):
        #Função para instanciar um objeto para adcionar no banco
        self.lus_dataHora = dataHora
        self.lus_acao = acao
        self.lme_mensagem = mensagem
        self.lte_idUsua = idUsua


#Tabela de Parametros
class CDA015(DB.Model):
    id_parametros = Column(Integer, primary_key=True, nullable=False)
    par_codigo = Column(String(10), nullable=False)
    par_valor = Column(String(10), nullable=False)


#Tabela de ligação Terceiro e Movimento Terceiro
class CDA016(DB.Model): 
    id = Column(Integer, primary_key=True, nullable=False)
    id_terceiro = Column(Integer, nullable=False)
    id_movTerc = Column(Integer, nullable=False)

    def __init__(self, idTerc: int, idMovTerc: int):
        #Função para instanciar um objeto para adcionar no banco
        self.id_terceiro = idTerc
        self.id_movTerc = idMovTerc