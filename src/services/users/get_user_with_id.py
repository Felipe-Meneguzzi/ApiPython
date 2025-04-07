from src.services.BaseService import BaseService, HTTPStatus
from src.repositories.UserRepository import UserRepository
repository = UserRepository()


class service():
    def get_user_with_id(id):
        try:
            id = int(id)
        except:
            return BaseService.send_exception(message="Formato de ID fornecido invalido, Digite apenas numeros", status_code=HTTPStatus.BAD_REQUEST)

        user = repository.get_user_by_id(id)
        if not user:
            return BaseService.send_response(data="Usuario nao encontrado.", status_code=HTTPStatus.NOT_FOUND)
        return BaseService.send_response(data=user.model_dump(), status_code=HTTPStatus.OK)
