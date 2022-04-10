from django.urls import path

from .views import CheckIfAuthenticated,Register

urlpatterns = [
    path('check-if-authenticated', CheckIfAuthenticated.as_view()),
    path('register-user', Register.as_view())
]
