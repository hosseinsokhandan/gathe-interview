from fastapi import FastAPI
from routers import member

from src import settings
from src.routers import document, permission


app = FastAPI()
app.include_router(member.router, prefix="/member")
app.include_router(document.router, prefix="/document")
app.include_router(permission.router, prefix="/permission")
