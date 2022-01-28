from flask import redirect, render_template, request
from amistades.models.model_user import Usuario
from amistades import app


@app.route('/addUser',methods=["POST"])
def addUser():
    user = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"]
    }
    resultado = Usuario.addUsuario(user)
    print(resultado)
    if resultado > 0:
        return redirect('/friendship')
