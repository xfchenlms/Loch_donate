from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
 path('', LoginView.as_view(template_name='login.html'), name='login'),
 path('signup/',views.signup, name='signup'),
]