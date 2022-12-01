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


@app.get("/about")
def about():
    return {"message": "This is the about page"}


@app.get("/account")
def index():
    return {}


@app.post("/login")
def login(login: str, password: str):
    return {"message": f"You logged in with {login}, and password: {password.upper()}"}


@app.get("/logout")
def logout():
    return {"message": "You have been logged out!"}


if __name__ == "__main__":
    uvicorn.run(app)
