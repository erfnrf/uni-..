from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    STID = Column(Integer, primary_key=True, index=True)
    FName = Column(String(10))
    LName = Column(String(10))
    FatherName = Column(String(10))
    Birth = Column(Date)
    IDS = Column(Integer)
    BornCity = Column(String(50))
    Address = Column(String(100))
    PostalCode = Column(String(10))
    CPhone = Column(String(15))
    HPhone = Column(String(15))
    Department = Column(String(50))
    Major = Column(String(50))
    Married = Column(String(10))
    SCourseIDs = Column(String(100))
    LIDs = Column(String(100))

class Professor(Base):
    __tablename__ = "professors"
    LID = Column(Integer, primary_key=True, index=True)
    FName = Column(String(10))
    LName = Column(String(10))
    ID = Column(Integer)
    Department = Column(String(50))
    Major = Column(String(50))
    Birth = Column(Date)
    BornCity = Column(String(50))
    Address = Column(String(100))
    PostalCode = Column(String(10))
    CPhone = Column(String(15))
    HPhone = Column(String(15))
    LCourseIDs = Column(String(100))

class Course(Base):
    __tablename__ = "courses"
    CID = Column(Integer, primary_key=True, index=True)
    CName = Column(String(25))
    Department = Column(String(50))
    Credit = Column(Integer)
