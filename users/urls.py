from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('singup/', views.SignUpView.as_view(), name="signup"),

]