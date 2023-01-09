
from django.urls import path
from .views import login_user, salir,guardar

urlpatterns = [
    path('', login_user ,name='login'),
    path('logout/', salir , name="logout"),
    path('guardar/', guardar , name="guardar"),
    
]
