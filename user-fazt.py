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