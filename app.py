from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

users = session.query(User).filter_by(id=25).one_or_none()

# Lê os dados já criados
"""for user in users:
    print(f"User id: {user.id}, User name: {user.name}")"""

# Atualiza os dados do usuário 
"""user3.name = "Bruno"
print(user3.name)

session.commit()"""

# Apaga usuário
session.delete(users)

session.commit()