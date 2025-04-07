from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from src.services.BaseService import BaseService, HTTPStatus


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        return await call_next(request)
