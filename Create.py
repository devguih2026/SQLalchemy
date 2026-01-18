from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

# Cria novos usuários
user = User(name = "Felipe")

session.add(user)

session.commit()