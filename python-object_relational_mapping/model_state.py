import sqlalchemy
from sqlalchemy import Column, Integer, String, DECIMAL, select, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
import copy

Base = declarative_base()
class User(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(DECIMAL(10, 20))
    quantity = Column(Integer)
    # addresses = relationship(
    #      "User2", back_populates="user", cascade="all, delete-orphan"
    #     )
    
class User2(Base):
    __tablename__ = "ep"


    id = Column(Integer, ForeignKey("employees.id"), primary_key=True, nullable=False)
    is_man = Column(Boolean)
    # user = relationship("User", back_populates="addresses")

engine = sqlalchemy.create_engine("mysql+mysqldb://root:@localhost/m_database")

Base.metadata.create_all(engine)
session = Session(engine)
# mango_boy = User(id=19, name= "g23g_po22p", rating= 10.2, quantity=23)
# session.add(mango_boy)
# session.commit()
users = session.execute(select(User, User2).join(User2)).all()
# users1 = [copy.copy(u[0]) for u in users]
u_1 = session.query(User).filter_by(id = 15).first()
# u_1.name = "coconutZen"
# session.commit()
# print(users[0][0].__dict__)
for u, p in users:
    print(u.__dict__, p.__dict__)
# for u in users:
#     print(u.__dict__)
#     session.delete(u)
# session.commit()
# session.delete(u_1)
# session.commit()