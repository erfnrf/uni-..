from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    FName: str = Field(..., max_length=10, pattern="^[ا-ی]+$")
    LName: str = Field(..., max_length=20, pattern="^[ا-ی]+$")
    FatherName: str = Field(..., max_length=20, pattern="^[ا-ی]+$")
    Birth: str = Field(..., pattern="^\d{4}-\d{2}-\d{2}$")
    IDS: int
    BornCity: str = Field(..., max_length=50, pattern="^[ا-ی\s]+$")
    Address: str = Field(..., max_length=255, pattern="^[ا-ی0-9\s]+$")
    PostalCode: str = Field(..., max_length=10, pattern="^\d{10}$")
    CPhone: str = Field(..., max_length=11, pattern="^09\d{9}$")
    HPhone: Optional[str] = Field(None, max_length=8, pattern="^\d{8}$")
    Department: str = Field(..., max_length=50, pattern="^[ا-ی\s]+$")
    Major: str = Field(..., max_length=50, pattern="^[ا-ی\s]+$")
    Married: str = Field(..., max_length=3, pattern="^(بله|خیر)$")
    SCourseIDs: str = Field(..., pattern="^(\d+,)*\d+$")
    LIDs: str = Field(..., pattern="^(\d+,)*\d+$")

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True

class ProfessorBase(BaseModel):
    # Similar updates here
    pass

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int

    class Config:
        from_attributes = True

class CourseBase(BaseModel):
    # Similar updates here
    pass

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True
