from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routers import students, professors, courses

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(students.router)
app.include_router(professors.router)
app.include_router(courses.router)

@app.get("/",)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/students")
def read_root(request: Request):
    return templates.TemplateResponse("index-students.html", {"request": request})
    
