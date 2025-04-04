from services.BaseService import BaseService, HTTPStatus

class service():
    def internal_server_error(exc: Exception):
        error_message = getattr(exc, "detail", str(exc))  # Usa 'str(exc)' como fallback
        return BaseService.send_exception(message=error_message, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)