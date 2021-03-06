from fastapi import FastAPI
from routers import document, permission, member
from db import init_db


app = FastAPI()
app.include_router(member.router, prefix="/member")
app.include_router(document.router, prefix="/document")
app.include_router(permission.router, prefix="/permission")


@app.on_event("startup")
async def startup_event():
    init_db(app)
