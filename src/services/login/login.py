from services.BaseService import BaseService, HTTPStatus
from repositories.UserRepository import UserRepository
from valueObjects.AuthTokenObject import create_token
from passlib.hash import bcrypt
repository = UserRepository()


class service():
    def login(body):
        if not body:
            return BaseService.send_response(data="Corpo da requisicao vazio", status_code=HTTPStatus.BAD_REQUEST)
        if not body.get('login'):
            return BaseService.send_response(data="Login nao informado", status_code=HTTPStatus.BAD_REQUEST)
        if not body.get('password'):
            return BaseService.send_response(data="Senha nao informada", status_code=HTTPStatus.BAD_REQUEST)

        login = body['login']
        user = repository.get_user_by_login(login)

        if not user:
            return BaseService.send_response(data="Usuario nao encontrado", status_code=HTTPStatus.NOT_FOUND)

        if not user.active:
            return BaseService.send_response(data="Usuario inativo", status_code=HTTPStatus.UNAUTHORIZED)

        if not bcrypt.verify(body['password'], user.password):
            return BaseService.send_response(data="Senha incorreta", status_code=HTTPStatus.UNAUTHORIZED)

        token = create_token(user)
        return BaseService.send_response(data={"token": token}, status_code=HTTPStatus.OK)
