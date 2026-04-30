from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school_student_id = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    year_level = models.SmallIntegerField()
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name