from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from src.valueObjects.AuthTokenObject import decode_token
from src.entities.RequestLogEntity import RequestLogEntity
from src.services.BaseService import BaseService, HTTPStatus
import datetime
import json


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        url = request.url.path
        url_params = json.dumps(dict(request.query_params))

        try:
            token = request.headers.get("Authorization")
            token_info = decode_token(token)
            request_user = token_info.get("user")
            request_user_id = request_user.get("id")
        except:
            request_user_id = 0

        try:
            body = await request.body()
            body = json.loads(body.decode("utf-8"))
            body = json.dumps(body)
        except:
            body = "Null"

        time = datetime.datetime.now()

        try:
            ip = request.client.host
        except:
            ip = "0"

        entity = RequestLogEntity(user_id=request_user_id, method=method, url=url, url_params=url_params, request_body=body, time=time, ip=ip)
        
        return BaseService.send_response(data=entity.model_dump(), status_code=HTTPStatus.UNAUTHORIZED)
    
        return await call_next(request)
