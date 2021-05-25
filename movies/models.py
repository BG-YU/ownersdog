from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from owners.models import Owner

class Dog(models.Model):
    name = CharField(max_length=45)
    age = IntegerField()
    owner = ForeignKey(Owner, on_delete=DO_NOTHING)

    class Meta:
        db_table = "movies"