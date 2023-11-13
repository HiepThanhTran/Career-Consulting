# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# class User(AbstractUser):
#     name = models.CharField(max_length=50, null=False)
#     email = models.CharField(max_length=50, null=False)
#     number_phone = models.IntegerField(null=True)
#     password = models.CharField(max_length=100, null=False)
#     created_date = models.DateTimeField(auto_now_add=True)
#     avatar = models.ImageField(upload_to='/upload/%Y/%m')
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name
