from rest_framework import serializers

from candidates.models import Candidate, Partylist
from elections.models import Election, Position, CourseValidItem, YearLevelValidItem
from facilitators.models import Facilitator
from schools.models import School
from students.models import Student, Course
from votes.models import Vote, VoteItem

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fiels = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'student_school_id', 'school', 'course', 'year_level', 'email']

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id']

    def validate_student_school_id(self, value):
        if Student.objects.filter(student_school_id=value).exists():
            raise serializers.ValidationError('Student Already Exists')
        return value