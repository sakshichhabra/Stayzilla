from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email_address, password=None, **kwargs):
        if not email_address:
            raise ValueError('Users must have a valid email address.')
        if not kwargs.get('user_id'):
            raise ValueError('Users must have a valid user id.')
        user = self.model(
            email_address=self.normalize_email(email_address), user_id=kwargs.get('user_id')
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


class Users(AbstractBaseUser):
    class Meta:
        managed = False
        db_table = 'USERS'

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    objects = UserManager()

    user_id = models.IntegerField(primary_key=True)
    password = models.TextField()
    email_address = models.EmailField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    last_login = models.DateField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email_address

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
