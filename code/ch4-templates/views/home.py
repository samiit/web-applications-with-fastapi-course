from fastapi_chameleon import template
import fastapi

router = fastapi.APIRouter()


@router.get(path="/")
@template(template_file="home/index.pt")
def index(user: str = "anon"):
    content = {"user_name": user.title()}
    return content


@router.get("/about")
def about():
    return {"message": "This is the about page"}
