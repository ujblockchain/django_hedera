from django.db.models.signals import post_save
from django.dispatch import receiver

from core.contract.utils.hedera.set_record import record_receipt

from .models import Contact


@receiver(post_save, sender=Contact)
def contract_deploy_store(sender, instance, created, **kwargs):
    # ensure instance has been created
    if created:
        # deploy contract and store record in hedera, this is get record if it exist
        receipt = record_receipt(instance.message_id, instance.name, instance.subject, instance.ref, instance.message)
        sender.objects.update(transaction_id=receipt.transactionId)
