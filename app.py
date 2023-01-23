from fastapi import FastAPI
from routes.user import user

app = FastAPI(title="Api de usuarios")
app.include_router(user)
