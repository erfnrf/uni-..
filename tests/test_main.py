import pytest

def test_read_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert "Welcome to the University Management System" in response.text

def test_create_student(test_client, db_session):
    response = test_client.post("/students/", json={"FName": "Ali", "LName": "Ahmadi"})
    assert response.status_code == 200
    data = response.json()
    assert data["FName"] == "Ali"
    assert data["LName"] == "Ahmadi"

def test_create_professor(test_client, db_session):
    response = test_client.post("/professors/", json={"FName": "Sara", "LName": "Jafari"})
    assert response.status_code == 200
    data = response.json()
    assert data["FName"] == "Sara"
    assert data["LName"] == "Jafari"

def test_create_course(test_client, db_session):
    response = test_client.post("/courses/", json={"name": "Math", "description": "Basic Math"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Math"
    assert data["description"] == "Basic Math"

def test_get_students(test_client, db_session):
    response = test_client.post("/students/", json={"FName": "Ali", "LName": "Ahmadi"})
    response = test_client.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["FName"] == "Ali"
    assert data[0]["LName"] == "Ahmadi"

def test_get_professors(test_client, db_session):
    response = test_client.post("/professors/", json={"FName": "Sara", "LName": "Jafari"})
    response = test_client.get("/professors/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["FName"] == "Sara"
    assert data[0]["LName"] == "Jafari"

def test_get_courses(test_client, db_session):
    response = test_client.post("/courses/", json={"name": "Math", "description": "Basic Math"})
    response = test_client.get("/courses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Math"
    assert data[0]["description"] == "Basic Math"
