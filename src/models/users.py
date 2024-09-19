from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# import base from database
from database.database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(String, primary_key=True)
	full_name = Column(String)
	email = Column(String, unique=True, nullable=False)
	hashed_password = Column(String, nullable=False)
	phone = Column(String)
	address = Column(String)
	role = Column(String, nullable=False)
	is_active = Column(Boolean, default=True)
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	last_updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

	hotels = relationship(relationship("Hotel", back_populates="owner"))
