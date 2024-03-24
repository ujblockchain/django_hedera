import json

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.contract.utils.hedera.set_record import record_receipt

from .models import Contact


@receiver(post_save, sender=Contact)
def contract_deploy_store(sender, instance, created, **kwargs):
    # ensure instance has been created
    if created:
        #
        message_stream = json.dumps([instance.name, instance.subject, instance.ref, instance.message])
        # deploy contract and store record in hedera, this is get record if it exist
        receipt = record_receipt(instance.message_id, message_stream)
        # store the transaction id in db
        sender.objects.update(transaction_id=receipt.transactionId)
        # send email
        send_mail(
            subject='New Blockchain transaction',
            message='A new message record has been stored on hedera testnet',
            from_email='test@example.com',
            recipient_list=['user@example.com'],
            fail_silently=False,
        )
