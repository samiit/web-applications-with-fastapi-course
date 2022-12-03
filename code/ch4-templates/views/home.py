from fastapi_chameleon import template
import fastapi

router = fastapi.APIRouter()


@router.get(path="/")
@template()  # you may as well skip mentioning the `template_file`, if folder structure maintained
def index(user: str = "anon"):
    content = {"user_name": user.title()}
    return content


@router.get("/about")
@template()
def about():
    return {"message": "This is the about page"}
