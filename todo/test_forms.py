from django.test import TestCase
from .forms import ItemForm


class TestItemform(TestCase):
    forms = ITemsForms{{'name',""}}
    self.assertfalse(form.is_valid())
    self.assertin('name', form.errors.keys())
    self.assertEqual(form.errors['name'][0],'This is the required field')