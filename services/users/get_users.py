from services.BaseService import BaseService, HTTPStatus
from repositories.UserRepository import UserRepository
repository = UserRepository()

class service():
    def get_users():
        users = repository.get_all_users()
        if not users:
            return BaseService.send_exception(message="Nenhum usuario encontrado.", status_code=HTTPStatus.NOT_FOUND)
        
        return BaseService.send_response(data=[user.model_dump() for user in users], status_code=HTTPStatus.OK)
        