import fastapi
import fastapi_chameleon
import uvicorn

from views import home, account, packages

app = fastapi.FastAPI()


def main():
    uvicorn.run(app)
    configure()


def configure():
    fastapi_chameleon.global_init("templates")
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == "__main__":
    main()
else:
    configure()
