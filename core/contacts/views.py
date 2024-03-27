from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView

from core.contacts.forms import ContactForm
from core.contract.utils.hedera.get_record import get_blockchain_record

from .models import Contact


class ContactHome(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    model = Contact
    success_url = 'details'
    success_message = 'message sent successfully'
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('details', args=[self.object.message_id])


class ContactDetails(View):

    def get(self, *args, **kwargs):
        get_message_id = self.kwargs.get('pk')
        template_name = 'details.html'

        # get record from hedera blockchain
        context = {
            'contract':
                get_blockchain_record(get_message_id),
            'transaction_id':
                Contact.objects.filter(message_id=get_message_id).values_list('transaction_id', flat=True)
        }

        return render(self.request, template_name, context)
