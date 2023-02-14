from django.contrib import admin
from .models import CustomUser,Saved

from django.contrib.auth.models import Group
# Register your models here.



# adimin paneldan Group  bo'limini olib tashlash uchun
admin.site.unregister(Group)


admin.site.register(CustomUser)
admin.site.register(Saved)