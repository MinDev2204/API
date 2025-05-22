from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.userName

class Category(models.Model):
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
