from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    #this will be for menu items, could add more here
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name


class SubstitutionOption(models.Model):
    #Here is the options for subbing out items, may need to make this ingredients?
    #need to think of better way to do this I think
    menu_item = models.ForeignKey(MenuItem,related_name='substitutions',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    extra_cost = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return f"{self.name} (+{self.extra_cost})"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed","Completed")
    ]

    server= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES, default = "pending")

    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL,null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.menu_item} (Order #{self.order.id})"
    