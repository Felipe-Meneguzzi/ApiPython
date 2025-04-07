from fastapi import Request
from starlette.exceptions import HTTPException as StarletteHTTPException


async def custom_route_not_found_exception_handler(request: Request, exc: StarletteHTTPException):
    from services.handlers.route_not_found import service
    return service.route_not_found()


async def custom_internal_server_error_handler(request: Request, exc: Exception):
    from services.handlers.internal_server_error import service
    return service.internal_server_error(exc)
