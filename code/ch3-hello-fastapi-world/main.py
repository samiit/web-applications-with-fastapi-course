import fastapi

app = fastapi.FastAPI()

@app.get(path="/")
def index():
    return "Hello World!"