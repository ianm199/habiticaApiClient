from src.client import HabiticaBaseClient
import requests

class HabiticaUserClient(HabiticaBaseClient):
    def register_local(self, username: str, email: str, password: str, confirmPassword: str):
        data = {"username": username, "email": email, "password": password, "confirmPassword": confirmPassword}
        return self.make_request('POST', '/user/auth/local/register', data=data)

    def login_local(self, username: str, password: str):
        data = {"username": username, "password": password}
        return self.make_request('POST', '/user/auth/local/login', data=data)

    def update_username(self, username: str, password: str = ''):
        data = {"username": username, "password": password}
        return self.make_request('PUT', '/user/auth/update-username', data=data)

    def update_password(self, password: str, newPassword: str, confirmPassword: str):
        data = {"password": password, "newPassword": newPassword, "confirmPassword": confirmPassword}
        return self.make_request('PUT', '/user/auth/update-password', data=data)

    def reset_password(self, email: str):
        data = {"email": email}
        return self.make_request('POST', '/user/reset-password', data=data)

    def update_email(self, newEmail: str, password: str):
        data = {"newEmail": newEmail, "password": password}
        return self.make_request('PUT', '/user/auth/update-email', data=data)

    def reset_password_set_new_one(self, newPassword: str, confirmPassword: str):
        data = {"newPassword": newPassword, "confirmPassword": confirmPassword}
        return self.make_request('POST', '/user/auth/reset-password-set-new-one', data=data)

    def delete_social(self, network: str):
        return self.make_request('DELETE', f'/user/auth/social/{network}')