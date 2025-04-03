from http import HTTPStatus
from fastapi.responses import JSONResponse

class BaseService:
    def send_exception(message: str, status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR, metadata: dict = None):
        response = BaseService.build_response_body(message, status_code, metadata)
        return JSONResponse(status_code=status_code, content=response)

    def send_response(data, status_code: HTTPStatus = HTTPStatus.OK, metadata: dict = None):
        response = BaseService.build_response_body(data, status_code, metadata)
        return JSONResponse(status_code=status_code, content=response)

    def build_response_body(data, status_code: HTTPStatus = HTTPStatus.OK, metadata: dict = None):
        return {
            "success": status_code.is_success,
            "status_code": status_code, 
            "data": data,
            "metadata": metadata
        }