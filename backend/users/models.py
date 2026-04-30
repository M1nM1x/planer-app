from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):    
    """Custom user model manager with email as the unique identifier"""
    
    def _create_user(self, email, password=None, **extra_fields):
        """Base method for creating a user"""
        
        if not email:
            raise ValueError("Email is not provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    
    def create_user(self, email, password=None, **extra_fields):    
        """Creates and saves a regular user with given email and password"""
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        
        return self._create_user(email, password, **extra_fields)
    
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and saves a superuser with given email and password"""
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    
    email = models.EmailField(max_length=50, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    