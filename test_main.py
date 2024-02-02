from fastapi.testclient import TestClient
from main import app

# app = FastAPI()

# @app.get("/")
# asunc def read_main():
#    return{"msg":"Hello World"}

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call/search or /wiki"}


def test_read():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json()["result"] == [
        "barack hussein obama ii",
        "bə-rahk hoo-sayn oh-bah-mə",
        "august",
        "american politician",
        "44th president"
    ]

