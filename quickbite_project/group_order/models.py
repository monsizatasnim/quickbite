from django.db import models
from accounts.models import User
from menu.models import MenuItem

class GroupOrder(models.Model):
    users = models.ManyToManyField(User)
    items = models.ManyToManyField(MenuItem)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)