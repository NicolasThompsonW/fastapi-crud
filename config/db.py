from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
# con = sqlite3.connect("tutorial.db")
# engine = create_engine(os.environ["RUTA_DATABASE"])
engine = create_engine(os.environ["RUTA_DATABASE2"], echo=True)

meta = MetaData()

conexion = engine.connect()
