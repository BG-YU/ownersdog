from django.db import models
from django.db.models.fields import CharField, IntegerField

class Owner(models.Model):
    name = CharField(max_length=45)
    email = CharField(max_length=300)
    age = IntegerField()

    class Meta:
        db_table = "owners"
