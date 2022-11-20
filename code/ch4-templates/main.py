import fastapi
import fastapi_chameleon
import uvicorn
from fastapi.responses import JSONResponse
from fastapi_chameleon import template

app = fastapi.FastAPI()

fastapi_chameleon.global_init("templates")


@app.get(path="/")
@template(template_file="index.html")
def index():
    user_name = "smathew"
    content = {"user_name": user_name}
    # return JSONResponse(content={"user_name": user_name})
    return content


if __name__ == "__main__":
    uvicorn.run(app)
