from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    school_id = models.IntegerField()
    complete_address = models.TextField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name