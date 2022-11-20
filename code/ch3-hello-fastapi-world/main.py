import fastapi
from fastapi.responses import JSONResponse

app = fastapi.FastAPI()


@app.get(path="/")
def index():
    return JSONResponse(content={"message": "Hello FastAPI course!"})


# if __name__ == "main":
#     uvicorn.run(app)
