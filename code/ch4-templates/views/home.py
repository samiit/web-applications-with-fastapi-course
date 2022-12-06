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
def about(company: str = "Unknown", year: int = 2000):
    return {
        "message": "Company Description",
        "company": company.title(),
        "year": year,
    }
