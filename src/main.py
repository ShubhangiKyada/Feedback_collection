from fastapi import FastAPI
from src.resource.authentication.api import auth_router
from src.resource.user.api import user_router
from src.resource.services.api import service_router
from src.resource.feedback.api import feedback_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(service_router)
app.include_router(feedback_router)