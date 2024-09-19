from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# import base from database
from database.database import Base

class Reservation(Base):
	__tablename__ = "reservations"

	id = Column(String, primary_key=True)
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	last_updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())