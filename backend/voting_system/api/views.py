from rest_framework import viewsets

from students.models import Student

from .serializer import StudentCreateSerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        student = self.request.query_params.get('student')

        if student:
            queryset = queryset.filter(student=student)
        
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StudentCreateSerializer
        return StudentSerializer