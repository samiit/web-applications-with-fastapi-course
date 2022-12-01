import fastapi
import fastapi_chameleon
import uvicorn
from fastapi_chameleon import template

app = fastapi.FastAPI()

fastapi_chameleon.global_init("templates")


@app.get(path="/")
@template(template_file="index.html")
def index(user: str = "anon"):
    content = {"user_name": user.title()}
    return content


if __name__ == "__main__":
    uvicorn.run(app)
