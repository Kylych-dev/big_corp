from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, role=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        if role is not None:
            user.set_role(role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_manager(self, email, password=None, **extra_fields):
        return self.create_user(
            email,
            role='manager',
            password=password,
            **extra_fields
        )

    def create_userprofile(self, email, password=None, **extra_fields):
        return self.create_user(
            email,
            role='user',
            password=password,
            **extra_fields
        )

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



