from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# import base from database
from database.database import Base

class Payment(Base):
	__tablename__ = "payments"

	id = Column(String, primary_key=True)
	amount = Column()