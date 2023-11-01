from app import db

class Perfil(db.Model):
    __tablename__ = 'perfil'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True)
    usuarios = db.Relationship('Usuario', backref='perfil')

    def __repr__(self):
        return f"Papel: {self.nome}"

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True, index=True)
    senha = db.Column(db.String(20))
    id_perfil = db.Column(db.Integer, db.ForeignKey('perfil.id'))

    def __repr__(self):
        return f"Usuário: {self.usuario}"