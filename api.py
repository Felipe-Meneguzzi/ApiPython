from fastapi import FastAPI, Depends
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import LoginRouter, UserRouter
from handlers.ExceptionsHandler import (
    custom_route_not_found_exception_handler,
    custom_internal_server_error_handler,
)
from middlewares.AuthMiddleware import AuthMiddleware

app = FastAPI()

# Registrar as rotass
app.include_router(router=UserRouter.router, prefix="/users",
                   dependencies=[Depends(AuthMiddleware)])

app.include_router(router=LoginRouter.router, prefix="/login")

# Registrar os handlers personalizados
app.add_exception_handler(StarletteHTTPException,
                          custom_route_not_found_exception_handler)
app.add_exception_handler(Exception, custom_internal_server_error_handler)
