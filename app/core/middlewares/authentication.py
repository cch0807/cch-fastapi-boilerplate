from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)


class AuthBackend(AuthenticationBackend):
    pass


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
