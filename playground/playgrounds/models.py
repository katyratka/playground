from django.db import models
from parks.models import Park

class Playground(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
