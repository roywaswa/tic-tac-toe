from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from uuid import UUID, uuid1
from utility.db import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    points: Mapped[int] = mapped_column(Integer)
    played_games: Mapped[int] = mapped_column(Integer)
    wins: Mapped[int] = mapped_column(Integer)

    @property
    def draw(self):
        return self.played_games - self.wins * 3

    @property
    def losses(self):
        return self.played_games - self.wins * 3 - self.draw

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r})"


class UserDBMethods:

    def __init__(self, orm_engine):
        self.session = sessionmaker(bind=orm_engine)()
        Base.metadata.create_all(bind=orm_engine)

    def get_user(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def get_all_users(self):
        return self.session.query(User).all()

    def register_user(self, username, password):
        user = User(
            id=uuid1(),
            username=username,
            password=password,
            points=0,
            played_games=0,
            wins=0
        )
        self.session.add(user)
        self.session.commit()
        return self.get_user(user.username)

    def update_user(self, user: User):
        """
        Updates the user in the database to match the given user object.
        :param user: User        :return: object: User
        """
        self.session.query(User).filter_by(username=user.username).update(
            {"points": user.points, "played_games": user.played_games, "wins": user.wins}
        )
        return self.get_user(user.username)
