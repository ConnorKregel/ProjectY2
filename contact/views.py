from django.conf import settings
from django.shortcuts import reverse, render
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.

class SuccessView(TemplateView):
    template_name = 'success.html'

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        full_message = f"message from {email}, {subject}, {message}"
        send_mail(
            subject = "receieved contact form submission",
            message = full_message,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [settings.NOTIFY_EMAIL],
        )
        
        return super(ContactView, self).form_valid(form)
        
def faq(request):
    return render(request, 'faq.html')
