from django.test import TestCase
from django.core import exceptions
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from employee.models import Employee


def create_employee(name: str, email: str,
                    department: str) -> Employee:
    return Employee.objects.create(name=name, email=email,
                                   department=department)


class EmployeeModelTest(TestCase):
    """ Tests the model of the Employee"""

    def test_employee_creation(self):
        """Tests the creation of the employee."""
        employee = create_employee('Test', 'test@test.com', 'TestDept')
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.name)

    def test_create_empty_fields(self):
        """Tests create the employee with blank values.
            Should raise an Validation exception.
        """
        employee = create_employee(
            name='', email='', department='')
        with self.assertRaises(exceptions.ValidationError):
            employee.clean_fields()

    def test_create_wrong_email(self):
        """Tests create the employee with wrong email format.
            Should raise an Validation exception.
        """
        employee = create_employee(
            name='Test', email='wrong_email', department='TestDept')
        with self.assertRaises(exceptions.ValidationError):
            employee.clean_fields()


class EmployeeViewTest(APITestCase):
    """ Make requests on the endpoint to test"""

    def test_list_employees(self):
        """ Test the list of the employees. """
        response = self.client.get(reverse('employee-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        """ Test the creation of the employees. """
        response = self.client.post(reverse('employee-list'),
                                    data={
                                        'name': 'Test',
                                        'email': 'test@test.com',
                                        'department': 'testDept'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_employee(self):
        employee = create_employee('Test', 'test@test.com', 'testDept')
        employee.save()
        response = self.client.delete(
            reverse('employee-detail', args=[employee.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
