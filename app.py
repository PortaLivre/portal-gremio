from flask import Flask, render_template, request, redirect, session

from models import db, Aviso
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

app.secret_key = app.config["SECRET_KEY"]

db.init_app(app)

@app.route("/")
def home():

    avisos = Aviso.query.order_by(Aviso.data.desc()).all()

    return render_template(
        "index.html",
        avisos=avisos
    )


@app.route("/eventos")
def eventos():
    return render_template("eventos.html")


@app.route("/noticias")
def noticias():
    return render_template("noticias.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if not session.get("admin"):
       return redirect("/entrar")

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]

        aviso = Aviso(
            titulo=titulo,
            descricao=descricao
        )

        db.session.add(aviso)
        db.session.commit()

        return redirect("/admin")

    avisos = Aviso.query.order_by(Aviso.data.desc()).all()

    return render_template(
        "admin.html",
        avisos=avisos
    )


@app.route("/entrar", methods=["GET", "POST"])
def entrar():

    if request.method == "POST":

        senha = request.form["senha"]

        if senha == app.config["ADMIN_PASSWORD"]:

            session["admin"] = True

            return redirect("/admin")

        return render_template(
            "entrar.html",
            erro="Senha incorreta!"
        )

    return render_template("entrar.html")


@app.route("/sair")
def sair():

    session.pop("admin", None)

    return redirect("/")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)