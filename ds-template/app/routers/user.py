from fastapi import APIRouter
from _const


router = APIRouter(prefix="/users")

@router.post(path="/sign-up", status_code=201, tags=[SwaggerTag])
def user_sign_up_handler(
    request: UserSignUp
):
    return UserSchema.from_orm(user)