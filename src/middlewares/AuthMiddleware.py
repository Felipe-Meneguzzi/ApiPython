from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from src.services.BaseService import BaseService, HTTPStatus
from src.valueObjects.AuthTokenObject import decode_token


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if not request.headers.get("Authorization"):
            return BaseService.send_response(data="Token nao informado", status_code=HTTPStatus.BAD_REQUEST)

        token = request.headers.get("Authorization")
        response = decode_token(token)

        if response == "E":
            return BaseService.send_response(data="Token expirado", status_code=HTTPStatus.UNAUTHORIZED)
        if response == "I":
            return BaseService.send_response(data="Token invalido", status_code=HTTPStatus.UNAUTHORIZED)

        return await call_next(request)
