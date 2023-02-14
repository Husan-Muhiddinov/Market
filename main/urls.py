from django.urls import path
from .views import IndexView,CategoryView


app_name='main'   #=> main:index ko'rinishida appga murojaat qilishimiz mumkin
urlpatterns=[
    path('', IndexView.as_view(),name='index'),
    path("<str:category_name>/category",CategoryView.as_view(),name='category'),
]