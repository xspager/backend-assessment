from django.db import models
from django.contrib.auth.models import AbstractUser

#class SystemUser(AbstractUser):
#    pass

class Conta(models.Model):
    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    # FIXME: Make number auto and start from a big number
    number = models.IntegerField()


class DebitoAutomatico(models.Model):

    # TODO: Localize?
    class StatusDebitoAutomatico(models.TextChoices):
        REQUESTED = "RE", "Requested"
        CANCELED = "CA", "Canceled"
        APROOVED = "AP", "Aprooved"
        REJECTED = "RJ", "Rejected"

    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=2,
        choices=StatusDebitoAutomatico.choices,
        default=StatusDebitoAutomatico.REQUESTED
    )
