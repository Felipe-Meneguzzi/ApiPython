from services.BaseService import BaseService, HTTPStatus


class service():
    def route_not_found():
        return BaseService.send_exception(message="Rota nao encontrada", status_code=HTTPStatus.NOT_FOUND)
