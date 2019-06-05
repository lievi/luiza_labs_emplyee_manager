from rest_framework import routers
from employee.views import EmployeeViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
