from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings


# Create your models here.


class UserManager(AbstractBaseUser):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an Email.')

        user = self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.isActive = True
        user.save(using=self._db)
        return user




class Users(AbstractBaseUser):
    email = models.EmailField(max_length = 255, verbose_name='email', unique = True)
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 100, null = True, blank = True)
    mobile = models.CharField(max_length = 50, db_index=True)
    
    ipAddress = models.GenericIPAddressField(null = True, blank = True)
    macAddress = models.CharField(max_length = 50, null = True, blank = True)
    
    verificationCode = models.CharField(max_length = 100, null = True, blank = True)
    isEmailVerified = models.BooleanField(default = False)
    verifiedOn = models.DateTimeField(null = True, blank = True)

    otpSent = models.CharField(max_length = 10, null = True, blank = True)
    isOTPVerified = models.BooleanField(default = False)
    otpVerifiedOn = models.DateTimeField(null = True, blank = True)

    isPassChanged = models.BooleanField(default = False)
    createdOn = models.DateTimeField(auto_now = True)    

    userType = models.CharField(max_length = 2, default='U')    # U: User, E: Emp., H: HR,
    is_admin = models.BooleanField(default = False)

    isActive = models.BooleanField(default = True)
    activatedBy = models.ForeignKey('self', blank=True, null=True, related_name='activatedByUser')
    activatedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    isAgree = models.BooleanField(default = True)

    isDeleted = models.BooleanField(default = False)
    updatedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)


    USERNAME_FIELD = 'email'





class UserLoginHistory(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL)
    ipAddress = models.GenericIPAddressField(null = True, blank = True)
    macAddress = models.CharField(max_length = 50, null = True, blank = True)
    loginTime = models.DateTimeField(auto_now = True)
    logoutTime = models.DateTimeField(null = True, blank = True)