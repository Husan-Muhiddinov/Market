from django.db import models
from users.models import CustomUser
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True,)
    title=models.CharField(max_length=150, null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=100000000, decimal_places=2, null=True)      # Mahsulot narxi o'nlik son  bo'lishi uchun DecimalField  ishlatiladi
    address=models.CharField(max_length=150, null=True)
    phone_number=models.CharField(max_length=17, null=True)
    tg_username=models.CharField(max_length=100, null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering=('-id',)
    


# Foydalanuvchi ixtiyoricha rasm yuklashi uchun

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to="product_images", null=True)



    

class Comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    body= models.CharField(max_length=150, null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return "Comment of" + str(self.author.username)