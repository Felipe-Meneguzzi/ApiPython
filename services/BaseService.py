from http import HTTPStatus
from fastapi.responses import JSONResponse
from valueObjects.ResponseBody import ResponseBody


class BaseService:
    def send_exception(message: str, status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR, metadata: dict = None):
        response = BaseService.build_response_body(
            message, status_code, metadata)
        return JSONResponse(status_code=status_code, content=response)

    def send_response(data, status_code: HTTPStatus = HTTPStatus.OK, metadata: dict = None):
        response = BaseService.build_response_body(data, status_code, metadata)
        return JSONResponse(status_code=status_code, content=response)

    def build_response_body(data, status_code: HTTPStatus = HTTPStatus.OK, metadata: dict = None):
        return ResponseBody(
            success=199 < status_code < 300,
            status_code=status_code,
            data=data,
            metadata=metadata
        ).model_dump()
