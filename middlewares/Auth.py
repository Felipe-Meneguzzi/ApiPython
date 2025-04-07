from fastapi import Request


async def AuthMiddleware(request: Request):
    print("AuthMiddleware: Verificando autenticacao")
