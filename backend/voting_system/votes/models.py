from django.db import models

from students.models import Student
from candidates.models import Candidate
from elections.models import Election, Position

class Vote(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
    )

class VoteItem(models.Model):
    vote = models.ForeignKey(
        Vote,
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
    )
