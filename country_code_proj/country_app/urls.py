# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'country_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('apidata/', views.country, name="country"),
]
