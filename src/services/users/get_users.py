from services.BaseService import BaseService, HTTPStatus
from repositories.UserRepository import UserRepository
from valueObjects.PageObject import PageObject
repository = UserRepository()


class service():
    def get_users(page_obj: PageObject = None):
        users = repository.get_all_users(page_obj)
        total_count = repository.get_total_count()
        metadata = {"total_count": total_count}
        if not users:
            return BaseService.send_exception(message="Nenhum usuario encontrado", status_code=HTTPStatus.NOT_FOUND)

        return BaseService.send_response(data=[user.model_dump() for user in users], status_code=HTTPStatus.OK, metadata=metadata)
