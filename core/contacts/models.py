from django.db import models
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField


class Contact(models.Model):
    message_id = ShortUUIDField(
        length=15,
        max_length=20,
        alphabet='abc1249856acbw',
        primary_key=True,
    )
    name = models.CharField(max_length=100, null=False, blank=False, help_text="user's name")
    subject = models.CharField(max_length=100, null=False, blank=False, help_text='message subject')
    reference = models.CharField(max_length=100, null=False, blank=False, help_text='message reference')
    message = models.CharField(max_length=500, null=False, blank=False, help_text='message')
    transaction_id = models.CharField(max_length=600, null=True, blank=True, help_text='blockchain transaction id')
    publish = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contract_id

    class Meta:
        ordering = ['date_created']
