from django.contrib.auth.backends import ModelBackend
from accounts.database.dbmanager import DBManager


class AuthenticationBackend(ModelBackend):

    def authenticate(self, email_address=None, password=None):
        if not email_address or not password:
            return None
        else:
            return DBManager.authenticate_user(email_address, password)

    def get_user(self, user_id):
        return DBManager.get_user(user_id)
