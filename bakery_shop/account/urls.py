from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.BakeryLogin.as_view(), name='login'),
    path('logout/', views.BakeryLogout.as_view(), name='logout'),
    path('register/', views.register_user, name='register'),
    path('register/activate/<int:number_phone>', views.activate_user, name='activate')
]
