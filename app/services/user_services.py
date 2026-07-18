from app.repositories.user_repository import UserRepository

class UserService:
    
    @staticmethod
    def get_all_user():
        return UserRepository.find_all()
    
    @staticmethod
    def create_user(data):
        return UserRepository.create(data)