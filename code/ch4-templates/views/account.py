from fastapi_chameleon import template
import fastapi

router = fastapi.APIRouter()


@router.get("/account")
def index():
    return {}


@router.post("/login")
def login(login: str, password: str):
    return {"message": f"You logged in with {login}, and password: {password.upper()}"}


@router.get("/logout")
def logout():
    return {"message": "You have been logged out!"}
