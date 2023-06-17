from flask import Blueprint, render_template

indexBlue = Blueprint("indexBlue", __name__)

#Rota o index do sistema
@indexBlue.route("/")
@indexBlue.route("/index")
def indeX():
    return render_template("index.html")