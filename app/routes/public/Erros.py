from flask import Blueprint, jsonify, render_template
import json

errosBlue = Blueprint("erros", __name__)

@errosBlue.app_errorhandler(404)
def notFound(erro):
    print(erro)
    return render_template("error/404.html"), 404


@errosBlue.app_errorhandler(500)
def serverError(erro):
    print(erro)
    return render_template("error/500.html"), 500