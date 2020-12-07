from django.db import models

# Create your models here.


class Labels(models.Model):
    LabelId = models.AutoField(primary_key=True)
    LabelName = models.CharField(max_length=100, blank=True, null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)
    Color = models.CharField(max_length=50, blank=True, null=True)
