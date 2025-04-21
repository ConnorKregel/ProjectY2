from django.urls import path
from .views import ContactView, SuccessView

app_name='contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
]