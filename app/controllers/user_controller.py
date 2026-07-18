from flask import jsonify
from app.services.user_services import UserService


class UserController:
    
    @staticmethod
    def get_users():
        users = UserService.get_all_users()
        
        return jsonify(users)
    
    @staticmethod
    def create_user():
        
        data = {
            "name":"Ali"
        }
        
        user = UserService.create_user(data)
        
        return jsonify(user), 201