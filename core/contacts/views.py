from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from core.contacts.forms import ContactForm

from .models import Contact


class ContactHome(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    model = Contact
    success_url = 'details'
    success_message = 'message id:%(message_id)s sent successfully'
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.message_id})


class ContactDetails(DetailView):
    model = Contact
    queryset = Contact.objects.filter(publish=True)
    template_name = 'details.html'
    context_object_name = 'contact'
