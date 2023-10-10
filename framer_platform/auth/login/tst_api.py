from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://myuser:mypassword@127.0.0.1:5432/mydatabase"
#
engine = create_engine(DATABASE_URL)

metadata = MetaData()

Base = declarative_base()


class User(Base):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    address = Column(String)
    is_framer = Column(Boolean)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据库连接
with engine.connect() as connection:
    # 创建表
    Base.metadata.create_all(engine)

    # 插入数据
    user = User(
        email="user1@example.com",
        username="user1",
        password="password",
        address="123 Street",
        is_framer=False,
    )
    session = SessionLocal()
    session.add(user)
    session.commit()

    # 查询数据
    users = session.query(User).all()
    for user in users:
        print("User:", user.username, "Email:", user.email)
