from fastapi import FastAPI, Depends
from starlette.middleware import Middleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.routers import LoginRouter, UserRouter
from src.middlewares.AuthMiddleware import AuthMiddleware
from src.middlewares.LogMiddleware import LogMiddleware
from src.handlers.ExceptionsHandler import (
    custom_route_not_found_exception_handler,
    custom_internal_server_error_handler,
)

auth_app = FastAPI(middleware=[Middleware(
    AuthMiddleware), Middleware(LogMiddleware)])
app = FastAPI(middleware=[Middleware(LogMiddleware)])

app.mount("/auth", auth_app)

app.add_exception_handler(StarletteHTTPException,
                          custom_route_not_found_exception_handler)
app.add_exception_handler(Exception, custom_internal_server_error_handler)

# Rotas com autenticação
auth_app.include_router(router=UserRouter.router, prefix="/users")

# Rotas sem autenticação
app.include_router(router=LoginRouter.router, prefix="/login")
