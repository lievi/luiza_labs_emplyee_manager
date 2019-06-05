from rest_framework import viewsets
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """API Endpoint that allow List, Add, and Delete
    the employees
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
