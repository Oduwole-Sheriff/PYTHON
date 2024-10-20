from django.test import TestCase
import pytest
from .models import Student
from django.db import IntegrityError
from .forms import StudentForm 
# Create your tests here.

@pytest.mark.parametrize(
    "age",
    [
        (9),
        (21)
    ]
)
def test_student_age(db, age):
    with pytest.raises(IntegrityError):
        Student.objects.create(firstname="fname", surname="sname", age=age, classroom=100, teacher="sir")

@pytest.mark.django_db
def test_student_form():
    data = {
        'firstname': 'asd',
        'surname': 'asd',
        'age': "21",
        'classroom': '100',
        'teacher': 'Sir'
    }

    form = StudentForm(data=data)
    assert False == form.is_valid()