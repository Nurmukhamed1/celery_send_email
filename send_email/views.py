from django.views.generic import CreateView

from send_email.forms import ContactForm
from send_email.models import Contact
from send_email.tasks import send_spam


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'send_email/contact.html'

    def form_valid(self, form):
        send_spam.delay(form.instance.email)
        return super().form_valid(form)
