from app import app, db

from models import *
from views import *

def criar_tabelas():
    with app.app_context():
        db.drop_all()
        db.create_all()

        admin = Perfil(nome="Admin")
        moderador = Perfil(nome="Moderador")
        usuario = Perfil(nome="Usuário")

        joao = Usuario(usuario='joao123', senha='jj112', perfil=admin)
        susan = Usuario(usuario='susan', senha='su21', perfil=usuario)
        denise = Usuario(usuario='denise99', senha='deni456', perfil=moderador)

        db.session.add(admin)
        db.session.add(moderador)
        db.session.add(usuario)

        db.session.add_all([joao, susan, denise])

        db.session.commit()
        '''
        print(admin.id)
        print(moderador.id)
        print(usuario.id)

        admin.nome = "Administrador"
        db.session.add(admin)
        db.session.commit()

        #db.session.delete(moderador)
        #db.session.commit()

        query = db.select(Perfil)
        perfis = db.session.execute(query)
        for perfil in perfis:
            print(perfil)


        query = db.select(Usuario)
        resultado = db.session.execute(query)

        print("Retornando todos os registros")
        for valor in resultado.all():
            print(valor)

        print("Retornando somente o primeiro valor")
        resultado = db.session.execute(query)
        for valor in resultado.first():
            print(valor)

        print("Retornando somente o primeiro valor como objeto e não lista")
        resultado = db.session.execute(query)
        print(resultado.scalar())

        # Selecionando os usuário com perfil id maior ou igual a 2
        query = db.select(Usuario.id, Usuario.usuario, Usuario.senha).where(Usuario.id >=2)
        resultado = db.session.execute(query)
        for val in resultado:
            print(val)

        # Ordenação
        query = db.select(Usuario).order_by(Usuario.usuario)
        resultado = db.session.execute(query)
        for val in resultado:
            print(val)

        # Joins
        query = db.select(Usuario, Perfil).join(Perfil.usuarios)
        resultado = db.session.execute(query)
        for val in resultado:
            print(val)

        query = db.select(Usuario.usuario, Usuario.senha, Perfil.nome).join(Perfil.usuarios)
        resultado = db.session.execute(query)
        for val in resultado:
            print(val)
        '''
if __name__ == '__main__':
    criar_tabelas()
    app.run(debug=True)