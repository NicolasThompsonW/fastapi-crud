from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.responses import JSONResponse
from config.db import conexion
from models.user import Users, Users2
from schemas.user import User
from cryptography.fernet import Fernet
from config.db import engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)
""" 
# Obtener todos los usuarios
@user.get("/users", response_model=list[User], tags=["users"])
async def get_users():
    return conexion.execute(Users.select()).fetchall()


# Agregar usuario
@user.post("/users", response_model=User, tags=["users"])
async def create_user(user: User):
    new_user = dict(name=user.name, email=user.email)
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conexion.execute(Users.insert().values(new_user))

    return new_user


# Obtener un usuario
@user.get("/users/{id}", response_model=User, tags=["users"])
async def get_user(id: int):
    resultado = conexion.execute(Users.select().where(Users.c.id == id)).first()
    return resultado


# Eliminar
@user.delete("/users/{id}", tags=["users"])
async def delete_user(id: int):
    try:
        resultado = conexion.execute(Users.delete().where(Users.c.id == id)).first()
        return f"Usuario {id} eliminado"
    except:
        return Response({"message": "usuario no encontrado"})


# Actualizar
@user.put("/users/{id}", response_model=User, tags=["users"])
async def put_user(id: int, user: User):
    password = f.encrypt(user.password.encode("utf8"))
    conexion.execute(
        Users.update()
        .values(name=user.name, email=user.email, password=password)
        .where(Users.c.id == id)
    )

    return dict(id=id, user=user.name, email=user.email, password=password) """


# ----------------- Con POO ------------------------------------#

# Obtener usuarios
@user.get("/users2")
async def get_users2():
    # Crea una nueva sesión de SQLAlchemy
    session = Session(bind=engine)
    # Realiza una consulta a la tabla "Users2" y recupera todos los registros de la tabla
    usuarios = session.query(Users2).all()
    # Cierra la sesión de SQLAlchemy, liberando los recursos utilizados por la sesión
    session.close()
    # devuelve el resultado de la consulta realizada, en este caso todos los objetos de la tabla "Users2"
    return usuarios


# Crear usuario
@user.post("/users2")
async def creando2(user: User):
    # Crea una sesión usando sessionmaker y el engine
    Session = sessionmaker(bind=engine)
    session = Session()
    # Encripta la contraseña con el metodo f.encrypt
    password = f.encrypt(user.password.encode("utf8"))
    # Crea una instancia de la clase Users2
    new_user = Users2(name=user.name, email=user.email, password=password)
    # Agrega la instancia a la sesión
    session.add(new_user)
    # Confirma la transacción
    session.commit()
    # Cierra la sesión
    session.close()

    # devuelve un diccionario con los atributos del objeto recien creado
    return dict(name=user.name, email=user.email, password=password)


# Obtener un usuario
@user.get(
    "/users2/{id}",
)
async def obteniendo_un_usuario(id):
    session = Session(bind=engine)
    resultado = session.query(Users2).get(id)
    diccionario = dict(
        id=resultado.id,
        name=resultado.name,
        email=resultado.email,
        password=resultado.password,
    )
    return vars(resultado)
    # return diccionario


# Eliminar usuario
@user.delete("/users2/{id}")
async def eliminar_usuario(id: int):
    session = Session(bind=engine)
    resultado = session.query(Users2).filter(Users2.id == id).delete()
    return f"Usuario {id} eliminado"
