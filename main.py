from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from repositorios import InsertarRepository
from routers import usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Esto permite que CUALQUIER página web envíe datos a tu API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router)

templates = Jinja2Templates(directory="Html")

@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse(name="index.html", request=request)
