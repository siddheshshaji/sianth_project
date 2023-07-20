from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('', views.index, name='index'),
    path('activate/<uid>/<token>', views.ActivateUser.as_view({'get': 'activation'}), name='activation'),
    #path('password-reset/<uid>/<token>', views.ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('account/login', views.index, name='index')
]