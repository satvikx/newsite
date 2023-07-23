from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('signup', views.signup_user, name = 'signup'),
    path('projects', views.home, name = 'projects'),
    path('notvalid', views.is_notvalid, name='valid'),
]
