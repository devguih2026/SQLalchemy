from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

my_sql_banco = "mysql+mysqlconnector://root:Guilherme!@localhost:3306/sqlalchemy"

engine = create_engine(my_sql_banco)

base = declarative_base()

class User(base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key= True)
    name = Column(String(255))

base.metadata.create_all(engine)