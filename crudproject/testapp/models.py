from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError

class Product(models.Model):
    product_name = models.CharField(max_length=150,validators=[MinLengthValidator(3,message="Product name must be at least 3 characters")])
    category = models.CharField(max_length=150,null=True,blank=True,validators=[MinLengthValidator(3,message="Category name must be at least 3 characters")])
    price = models.FloatField(validators=[MinValueValidator(0,message="Price must be at least 0")])
    quantity = models.IntegerField(validators=[MinValueValidator(0,message="Quantity must be at least 0")])
    supplier = models.CharField(max_length=150,null=True,blank=True,validators=[MinLengthValidator(3,message="Supplier name must be at least 3 characters")])
    minimum_stock_level = models.IntegerField(null=True,blank=True,validators=[MinValueValidator(0, message="Minimum stock level must be at least 0")])

    def clean(self):
        errors = {}
        if not self.product_name or not self.product_name.strip():
            errors["product_name"] = "Product name is required."

        elif self.product_name.lower() == "admin":
            errors["product_name"] = "Admin is not a valid product name."

        if not self.category or not self.category.strip():
            errors["category"] = "Category is required."

        if self.price is None:
            errors["price"] = "Price is required."

        if self.quantity is None:
            errors["quantity"] = "Quantity is required."

        if not self.supplier or not self.supplier.strip():
            errors["supplier"] = "Supplier is required."

        if self.minimum_stock_level is None:
            errors["minimum_stock_level"] = (
                "Minimum stock level is required."
            )

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.product_name