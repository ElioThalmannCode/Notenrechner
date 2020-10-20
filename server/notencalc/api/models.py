from django.db import models

# Create your models here.
class Note(models.Model):
    bezeichnung = models.CharField(max_length=100)
    notenwert = models.DecimalField(max_digits=3, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bezeichnung