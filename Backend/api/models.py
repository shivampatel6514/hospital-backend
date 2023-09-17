from django.db import models
import uuid

# Create your models here.


class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role_type = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    specilist = models.CharField(max_length=255,null=True)
    degree = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'