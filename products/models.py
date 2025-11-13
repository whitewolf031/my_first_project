from django.db import models

class ProductsList(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField(max_length=100)
    product_sklad = models.BooleanField(default=False)
    product_size = models.IntegerField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name}, {self.product_price}"