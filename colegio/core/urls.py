from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.anotaciones,name='anotaciones'),
    path('asistencia',views.asistencia,name='asistencia'),
    path('login',views.login,name='login'),
    path('menu',views.menu,name='menu'),
    path('notas',views.notas,name='notas'),
]