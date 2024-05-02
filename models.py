import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    __abstract__ = True

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

class Task(DeclarativeBase):
    __tablename__ = 'task'
    id: Mapped[int]= mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()
    property: Mapped[int ] = mapped_column()

