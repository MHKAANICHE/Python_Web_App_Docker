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
    response = client.get("/wiki/Barack Obama")
    assert response.status_code == 200
    # Update the expected list to include 'Barack (disambiguation)' at index 5
    assert (
        response.json()["result"]
        == "Barack Hussein Obama II (  bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician who served as the 44th president of the United States from 2009 to 2017."
    )
