from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
from sqlalchemy.orm import declarative_base
import json

Base = declarative_base()


Users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
)


class Users2(Base):
    __tablename__ = "users2"
    id = Column(Integer, primary_key=True)
    name = Column(String(225))
    email = Column(String(255))
    password = Column(String(255))


meta.create_all(engine)
Base.metadata.create_all(bind=engine)
