import fastapi
from fastapi.responses import JSONResponse
import uvicorn

app = fastapi.FastAPI()


@app.get(path="/")
def index():
    return JSONResponse(content={"message": "Hello FastAPI!"})


if __name__ == "main":
    uvicorn.run(app)
