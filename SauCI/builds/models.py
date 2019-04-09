from django.db import models
import uuid

# Create your models here.

class Build(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)