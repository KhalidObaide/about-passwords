from django.contrib import admin
from django.urls import path
from home import views as home_views

urlpatterns = [
    # about_password.com/
    path('', home_views.index, name='index'),

    # about_password.com/admin
    path('admin/', admin.site.urls),
]
