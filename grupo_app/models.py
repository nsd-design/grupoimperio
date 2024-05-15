from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Utilisateur(AbstractUser):
    telephone = PhoneNumberField()

    def __str__(self):
        return f"{self.username} | {self.telephone}"


class CouponCode(models.Model):
    coupon_choice = [
        (1, "BITNOVO"),
        (2, "PCS")
    ]
    coupon = models.CharField(max_length=15)
    coupon_type = models.SmallIntegerField(choices=coupon_choice)
    created_by = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by}  {self.coupon} - {self.coupon_type}"
