from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import users, login
from handlers.exceptions import (
    custom_route_not_found_exception_handler,
    custom_internal_server_error_handler,
)

app = FastAPI()

# Registrar as rotas
app.include_router(users.router)
app.include_router(login.router)

# Registrar os handlers personalizados
app.add_exception_handler(StarletteHTTPException,
                          custom_route_not_found_exception_handler)
app.add_exception_handler(Exception, custom_internal_server_error_handler)
