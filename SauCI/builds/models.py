from django.db import models
import uuid

# Create your models here.

class Build(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"Build {self.id}: completed: {self.completed}. created_at: {self.created_at}, completed_at: {self.completed_at}"