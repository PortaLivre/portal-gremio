# Aqui ficarão os modelos do banco de dados.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Aviso(db.Model):
    __tablename__ = "avisos"

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(100), nullable=False)

    descricao = db.Column(db.Text, nullable=False)

    data = db.Column(db.DateTime, default=datetime.utcnow)