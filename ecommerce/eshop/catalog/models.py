from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    index = models.IntegerField(default=1)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
