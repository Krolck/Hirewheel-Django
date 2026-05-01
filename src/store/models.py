from django.db import models
from django.conf import settings
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2,max_digits=12)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return [self.name, self.description, self.date]
    
class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.product.name}"