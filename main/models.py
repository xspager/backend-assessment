from django.db import models
from django.contrib.auth.models import AbstractUser

#class SystemUser(AbstractUser):
#    pass


# TODO: Implement logic delete logic for the base model and manager
class CustomModel(models.Model):
    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        abstract=True


class Partner(CustomModel):
    name = models.CharField(max_length=300)
    # FIXME: Make number auto and start from a big number
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(CustomModel):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Activation(CustomModel):

    # TODO: Localize?
    class StatusActivation(models.TextChoices):
        REQUESTED = "RE", "Requested"
        CANCELED = "CA", "Canceled"
        APROOVED = "AP", "Aprooved"
        REJECTED = "RJ", "Rejected"

    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=2,
        choices=StatusActivation.choices,
        default=StatusActivation.REQUESTED
    )

    def __str__(self):
        return f"Direct debt from {self.partner.name} for {self.customer.name}"
