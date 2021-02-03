import uuid
from sqlalchemy import Column, String, Table, ForeignKey
from .config import Base

# from sqlalchemy.orm import relationship, backref

from fancy_todo_list.application.entities import User, RefId, Username


class UserModel(Base):
    __tablename__ = "users"
    ref_id = Column("id", String(36), primary_key=True)
    username = Column("username", String(20), unique=True, nullable=False)
    # books = relationship("Book", backref=backref("author"))
    # publishers = relationship(
    #     "Publisher", secondary=author_publisher, back_populates="authors"
    # )

    @classmethod
    def create_from(cls, user: User) -> "UserModel":
        return UserModel(ref_id=user.ref_id.value.hex, username=user.username.value)

    def to_entity(self) -> User:
        ref_id = RefId.create(uuid.UUID(self.ref_id, version=4))
        username = Username.create(self.username)

        return User(ref_id, username)
