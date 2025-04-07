from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import Users, Login
from handlers.Exceptions import (
    custom_route_not_found_exception_handler,
    custom_internal_server_error_handler,
)

app = FastAPI()

# Registrar as rotass
app.include_router(Users.router)
app.include_router(Login.router)

# Registrar os handlers personalizados
app.add_exception_handler(StarletteHTTPException,
                          custom_route_not_found_exception_handler)
app.add_exception_handler(Exception, custom_internal_server_error_handler)
