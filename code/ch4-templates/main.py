import fastapi
import uvicorn
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()


@app.get(path="/")
def index():
    content = """
    <h1>First HTML response</h1>
    <div>Hello FastAPI course! Now we're getting into HTML responses with templating!</div>
    <p> There are three templating frameworks we'll assess: </p>
    <ol>
        <li><a href="https://jinja.palletsprojects.com/en/3.1.x/" target="_" rel="noopener noreferrer">Jinja2</a></li>
        <li><a href="https://www.makotemplates.org/" target="_" rel="noopener noreferrer">Mako</a></li>
        <li><a href="https://chameleon.readthedocs.io/en/latest/" target="_" rel="noopener noreferrer">Chameleon</a></li>
    </ol>
    And the winner for this course is Chameleon.
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app)
