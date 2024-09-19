from sqlalchemy import Boolean, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# import base from database
from src.database.database import Base

class Hotel(Base):
	__tablename__ = "hotels"

	id = Column(String, primary_key=True)
	name = Column(String, nullable=False)
	address = Column(String)
	owner_id = Column(String, ForeignKey("users.id"))
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	last_updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

	owner = relationship(relationship("User", back_populates="hotels"))