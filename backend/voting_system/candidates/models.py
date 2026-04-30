from django.db import models

from students.models import Student
from elections.models import Election, Position

class Partylist(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f'{self.election.__str__()} Partylist: {self.name}'

class Candidate(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
    )
    partlist = models.ForeignKey(
        Partylist,
        on_delete=models.CASCADE,
        null=True
    )
    image_file = models.ImageField(
        upload_to='',
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.election.__str__()} Candidate: {self.student.__str__()}'

