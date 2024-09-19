from sqlalchemy import Boolean, Column, String, DateTime, ForeignKey
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
	# role = Column(String, nullable=)
	# hotel_id = Column(String, ForeignKey("hotels.id"), nullable=True)
	is_active = Column(Boolean, default=True)
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	last_updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
	hotels = relationship("Hotel", backref="users")

	def __repr__(self):
		return f"<User(full_name={self.full_name}, email={self.email})>"