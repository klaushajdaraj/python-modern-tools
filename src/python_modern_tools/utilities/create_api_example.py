"""Create API example."""

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Root endpoint returning a message."""
    return {"message": "This is an example API created using FastAPI!"}


@app.get("/csv")
def read_csv() -> Response:
    """CSV endpoint returning a message."""
    csv_content = "id,name,age\n1,Alice,30\n2,Bob,25\n3,Charlie,35"
    return Response(content=csv_content, media_type="text/plain")
