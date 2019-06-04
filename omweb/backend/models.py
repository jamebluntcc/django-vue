from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "<Book {0}>".format(self.id)


