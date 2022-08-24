from app.domain.entity import User

# user 생성 로직
def create_user(user_name: str):
    user = User(name=user_name)
    return user