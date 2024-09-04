from sqlalchemy import Column, String

from database import Base, get_id_type_for_dialect


class Item(Base):
    __tablename__ = 'example_items'
    id = Column(get_id_type_for_dialect(), primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
