from flask import Blueprint, jsonify
import json

erros = Blueprint("erros", __name__)

@erros.errorhandler(404)
def notFound(erro):
    pass


@erros.errorhandler(500)
def serverError(erro):
    pass