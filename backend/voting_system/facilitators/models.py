from django.db import models

from schools.models import School

class Facilitator(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school_staff_id = models.CharField(max_length=255)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name