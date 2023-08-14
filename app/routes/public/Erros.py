from flask import Blueprint, render_template

errosBlue = Blueprint("erros", __name__)

@errosBlue.app_errorhandler(404)
def notFound(erro):
    print(erro)
    return render_template("public/error/404.html"), 404


@errosBlue.app_errorhandler(500)
def serverError(erro):
    print(erro)
    return render_template("public/error/500.html"), 500


@errosBlue.route("/error_500")
def serverERROR():
    return render_template("public/error/500.html"), 500


@errosBlue.route("/error_404")
def notFOUND():
    return render_template("public/error/404.html"), 404