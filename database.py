from sqlalchemy import create_engine, Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from datetime import datetime

# SQLite database URL (in-memory database)
DATABASE_URL = "sqlite:///ticketingsystemdb"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Single session
Session = SessionLocal()

# Create a base class for our SQLAlchemy models
Base = declarative_base()

# class User(Base):
# 	__tablename__ = "user"
# 	user_id = Column(Integer, primary_key=True, index=True)
# 	name = Column(String)
# 	email = Column(String)
# 	contact = Column(String)

# 	booked_user = relationship("Booking", back_populates="booked_user")

# class Stadium(Base):
# 	__tablename__ = "stadium"
# 	stadium_id = Column(Integer, primary_key=True, index=True)
# 	name = Column(String)
# 	city = Column(String)
# 	state = Column(String)
# 	seat_capacity = Column(String)

# 	matches = relationship("Match", back_populates="stadium")
# 	seatings = relationship("Seating", back_populates="stadium")


# class Match(Base):
# 	__tablename__ = "match"
# 	match_id = Column(Integer, primary_key=True, index=True)
# 	match_date = Column(Date)
# 	match_time = Column(String)
# 	match_name = Column(String)
# 	stadium_id = Column(Integer, ForeignKey("stadium.stadium_id"))

# 	stadium = relationship("Stadium", back_populates="matches")
# 	booked_match = relationship("Booking", back_populates="booked_match")

# class Seating(Base):
# 	__tablename__ = "seating"
# 	seat_id = Column(Integer, primary_key=True, index=True)
# 	stadium_id = Column(Integer, ForeignKey("stadium.stadium_id"))
# 	stand_name = Column(String)
# 	seat_number = Column(String)

# 	stadium = relationship("Stadium", back_populates="seatings")
# 	booked_seating = relationship("Booking", back_populates="booked_seating")


# class Booking(Base):
# 	__tablename__ = "booking"
# 	booking_number = Column(String)
# 	match_id = Column(Integer, ForeignKey("match.match_id"), primary_key=True)
# 	seat_id = Column(Integer, ForeignKey("seating.seat_id"), primary_key=True)
# 	user_id = Column(Integer, ForeignKey("user.user_id"))
# 	created_on = Column(TIMESTAMP, default=datetime.utcnow)

# 	booked_match = relationship("Match", back_populates="booked_match")
# 	booked_seating = relationship("Seating", back_populates="booked_seating")
# 	booked_user = relationship("User", back_populates="booked_user")


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    contact = Column(String)

    booked_bookings = relationship("Booking", back_populates="booked_user")

class Stadium(Base):
    __tablename__ = "stadium"
    stadium_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    state = Column(String)
    seat_capacity = Column(Integer)

    matches = relationship("Match", back_populates="stadium")
    seatings = relationship("Seating", back_populates="stadium")

class Match(Base):
    __tablename__ = "match"
    match_id = Column(Integer, primary_key=True, index=True)
    match_date = Column(Date)
    match_time = Column(String)
    match_name = Column(String)
    stadium_id = Column(Integer, ForeignKey("stadium.stadium_id"))

    stadium = relationship("Stadium", back_populates="matches")
    booked_bookings = relationship("Booking", back_populates="booked_match")

class Seating(Base):
    __tablename__ = "seating"
    seat_id = Column(Integer, primary_key=True, index=True)
    stadium_id = Column(Integer, ForeignKey("stadium.stadium_id"))
    stand_name = Column(String)
    seat_number = Column(String)

    stadium = relationship("Stadium", back_populates="seatings")
    booked_bookings = relationship("Booking", back_populates="booked_seating")

class Booking(Base):
    __tablename__ = "booking"
    booking_number = Column(String, primary_key=True)
    match_id = Column(Integer, ForeignKey("match.match_id"), primary_key=True)
    seat_id = Column(Integer, ForeignKey("seating.seat_id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    created_on = Column(TIMESTAMP, default=datetime.utcnow)

    booked_match = relationship("Match", back_populates="booked_bookings")
    booked_seating = relationship("Seating", back_populates="booked_bookings")
    booked_user = relationship("User", back_populates="booked_bookings")


def create_tables():
	Base.metadata.create_all(bind=engine)
