from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Manager that helps you to filter or do some actions
    with the model
    """

    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True
        user.set_password(password)
        user.save(using=self._db)
        return user
