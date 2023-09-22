from flask import Blueprint, render_template

errosBlue = Blueprint("errosBlue", __name__)

@errosBlue.app_errorhandler(404)
def notFound(erro):
    return render_template("public/error/404.html"), 404


@errosBlue.app_errorhandler(405)
def methodNotAllowed(erro):
    return render_template("public/error/405.html"), 405


@errosBlue.app_errorhandler(500)
def serverError(erro):
    return render_template("public/error/500.html"), 500


@errosBlue.route("/error_500")
def serverERROR():
    return render_template("public/error/500.html"), 500


@errosBlue.route("/error_404")
def notFOUND():
    return render_template("public/error/404.html"), 404


@errosBlue.route("/error_405")
def methodNOTALLOWED():
    return render_template("public/error/405.html"), 404