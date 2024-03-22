from django.db import models
from django.utils import timezone


class DeployedContract(models.Model):
    contract_id = models.CharField(max_length=500, help_text='deployed contract id')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contract_id

    class Meta:
        verbose_name = 'Deployed Contract'
        verbose_name_plural = 'Deployed Contract'
