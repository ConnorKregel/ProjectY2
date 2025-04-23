from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path('password-change/',PasswordChangeView.as_view(success_url=reverse_lazy('home')),name='password_change'),
]