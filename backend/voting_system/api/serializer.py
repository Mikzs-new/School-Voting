from rest_framework import serializers

from candidates.models import Candidate, Partylist
from elections.models import Election, Position, CourseValidItem, YearLevelValidItem
from facilitators.models import Facilitator
from schools.models import School
from students.models import Student, Course
from votes.models import Vote, VoteItem

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

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

class FacilitatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilitator
        fields = '__all__'

class FacilitatorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilitator
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class PositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class CourseValidItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseValidItem
        fields = '__all__'

class CourseValidItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseValidItem
        fields = '__all__'

class YLValidItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearLevelValidItem
        fields = '__all__'

class YLValidItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearLevelValidItem
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class CandidateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class PartylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partylist
        fields = '__all__'

class PartylistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partylist
        fields = '__all__'

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

class ElectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

class VoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteItem
        fields = '__all__'

class VoteItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteItem
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class VoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'



    
