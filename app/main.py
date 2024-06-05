from fastapi import FastAPI
from app.routers import students, professors, courses
from app.database import engine, Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(students.router)
app.include_router(professors.router)
app.include_router(courses.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project"}