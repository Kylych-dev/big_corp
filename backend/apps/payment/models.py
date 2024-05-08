from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from ..account.models import CustomUser
from ..product.models import Product


class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_("Full name"))
    email = models.EmailField(max_length=255, verbose_name=_("Email"))

    street_address = models.CharField(max_length=255, verbose_name=_("Street Address"))
    apartment_address = models.CharField(max_length=255, verbose_name=_("Apartment Address"))
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("User")
    )
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("City"))
    zip_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Zip Code"))

    def __str__(self):
        # return self.full_name
        return 'Shipping Address: {}'.format(self.id)

    class Meta:
        verbose_name = _("Shipping Address")
        verbose_name_plural = _("Shipping Addresses")


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("User"))
    shipping_address = models.ForeignKey(
        ShippingAddress,
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name=_("Shipping Address")
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    paid = models.BooleanField(default=False, verbose_name=_("Paid"))
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_("Discount")
    )

    def __str__(self):
        return 'Order: {}'.format(self.id)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Product"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    quantity = models.IntegerField(default=1, verbose_name=_("Quantity"))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("User"))

    def __str__(self):
        return 'OrderItem: {}'.format(self.id)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ['-id']
