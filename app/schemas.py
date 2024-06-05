from pydantic import BaseModel, Field
from typing import List
from datetime import date

class StudentBase(BaseModel):
    FName: str = Field(..., max_length=10, regex="^[ا-ی]+$")
    LName: str = Field(..., max_length=10, regex="^[ا-ی]+$")
    FatherName: str = Field(..., max_length=10, regex="^[ا-ی]+$")
    Birth: date
    IDS: int = Field(..., ge=100, le=999)
    BornCity: str
    Address: str = Field(..., max_length=100)
    PostalCode: str = Field(..., regex="^\d{10}$")
    CPhone: str = Field(..., regex="^09\d{9}$")
    HPhone: str = Field(..., regex="^\d{8}$")
    Department: str
    Major: str
    Married: str
    SCourseIDs: str
    LIDs: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    STID: int

    class Config:
        orm_mode = True

class ProfessorBase(BaseModel):
    FName: str = Field(..., max_length=10, regex="^[ا-ی]+$")
    LName: str = Field(..., max_length=10, regex="^[ا-ی]+$")
    ID: int
    Department: str
    Major: str
    Birth: date
    BornCity: str
    Address: str = Field(..., max_length=100)
    PostalCode: str = Field(..., regex="^\d{10}$")
    CPhone: str = Field(..., regex="^09\d{9}$")
    HPhone: str = Field(..., regex="^\d{8}$")
    LCourseIDs: str

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    LID: int

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    CName: str = Field(..., max_length=25, regex="^[ا-ی]+$")
    Department: str
    Credit: int = Field(..., ge=1, le=4)

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    CID: int

    class Config:
        orm_mode = True
