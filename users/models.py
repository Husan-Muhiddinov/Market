from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=17, null=True)
    tg_username=models.CharField(max_length=150, unique=True, null=True)
    avatar=models.ImageField(upload_to='avatars/', default='avatars/default.png', null=True)


    # USERNAME_FIELD = 'tg_username'

    def __str__(self):
        return str(self.username)
    


class Saved(models.Model):
    product=models.ForeignKey("products.Product",on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    date=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return "Comment of" + str(self.author.username)