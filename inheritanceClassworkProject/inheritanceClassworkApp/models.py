from django.db import models

# Contact Model
class ContactModel(models.Model):
    name = models.CharField(max_length=100, default=0)
    email = models.EmailField(max_length=100, default="")

