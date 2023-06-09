from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import login_view,logout_view

urlpatterns = [
   path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('anotaciones',views.anotaciones,name='anotaciones'),
    path('menu',views.menu,name='menu'),
    path('asistencia',views.asistencia,name='asistencia'),
    path('donacion',views.donacion,name='donacion'),
    path('menu',views.menu,name='menu'),
    path('notas',views.notas,name='notas'),
    path('registro/', views.registro, name='registro'),
]