from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomPasswordChangeForm
from .models import CustomUser

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('shop:all_products')

    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)

        # Add user to the Customer group
        customer_group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(customer_group)

        # Log the user in after signup
        login(self.request, self.object)

        return response  # Redirect to success URL
    
class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('shop:all_products')