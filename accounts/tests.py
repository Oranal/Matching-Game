from django.test import TestCase
from accounts.models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        self.kinder = Account.objects.get_or_create(
            username='KindergardenTest',
            first_name='FirstNameKinderTest',
            last_name='LastNameKinderTest',
            password='test',
            institution='InstitutionTest',
            role='Kindergarden',
        )[0]
        
        self.child = Account.objects.get_or_create(
            username='ChildTest',
            first_name='FirstNameChildTest',
            last_name='LastNameChildTest',
            password='test',
            institution='InstitutionTest',
            rating=0,
            role='Child',
        )[0]

        self.admin = Account.objects.get_or_create(
            username='AdminTest',
            first_name='FirstNameAdminTest',
            last_name='LastNameAdminTest',
            password='test',
            institution='InstitutionTest',
            role='Administrator',
        )[0]

    def test_permissionTest(self):
        self.assertEqual(self.kinder.get_permission(), 'Limited')
        self.assertEqual(self.child.get_permission(), 'Player')
        self.assertEqual(self.admin.get_permission(), 'All')

    def test_fields_assigned_properly(self):
        # Kindergarden's fields
        self.assertEqual(self.kinder.username, 'KindergardenTest')
        self.assertEqual(self.kinder.password, 'test')
        self.assertEqual(self.kinder.first_name, 'FirstNameKinderTest')
        self.assertEqual(self.kinder.last_name, 'LastNameKinderTest')
        self.assertEqual(self.kinder.institution, 'InstitutionTest')
        self.assertEqual(self.kinder.role, 'Kindergarden')

        # Child's fields
        self.assertEqual(self.child.username, 'ChildTest')
        self.assertEqual(self.child.password, 'test')
        self.assertEqual(self.child.first_name, 'FirstNameChildTest')
        self.assertEqual(self.child.last_name, 'LastNameChildTest')
        self.assertEqual(self.child.institution, 'InstitutionTest')
        self.assertEqual(self.child.role, 'Child')
        self.assertEqual(self.child.rating, 0)

        # Admin's fields
        self.assertEqual(self.admin.username, 'AdminTest')
        self.assertEqual(self.admin.password, 'test')
        self.assertEqual(self.admin.first_name, 'FirstNameAdminTest')
        self.assertEqual(self.admin.last_name, 'LastNameAdminTest')
        self.assertEqual(self.admin.institution, 'InstitutionTest')
        self.assertEqual(self.admin.role, 'Administrator')


    
