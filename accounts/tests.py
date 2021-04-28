from django.test import TestCase 
from django.urls import resolve
from django.urls import reverse
from accounts.models import Account
from accounts.views import *

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

class AccountsUrlsTest(TestCase):
    def test_admin_dashboard_url_resolved(self):
        #Act
        url = reverse('admin_dashboard')
        #Assert
        self.assertEqual(resolve(url).func, admin_dashboard)

    def test_games_url_resolved(self):
        #act
        url = reverse('games')
        #Assert
        self.assertEqual(resolve(url).func,games)


    def test_difficulty_url_resolved(self):
        #Act
        url = reverse('difficulty')
        #Assert
        self.assertEqual(resolve(url).func,difficulty)
    
    def test_new_game_url_resolved(self):
        #Act
        url = reverse('new_game')
        #Assert
        self.assertEqual(resolve(url).func,new_game)

    def test_game_info_url_resolved(self):
        #Act
        url = reverse('game_info')
        #Assert
        self.assertEqual(resolve(url).func,game_info)

    def test_game_topic_url_resolved(self):
        #Act
        url = reverse('game_topic')
        #Assert
        self.assertEqual(resolve(url).func,game_topic)

    def test_extra_card_url_resolved(self):
        #Act
        url = reverse('extra_card')
        #Assert
        self.assertEqual(resolve(url).func,extra_card)

    def test_done_extra_url_resolved(self):
        #Act
        url = reverse('done_extra')
        #Assert
        self.assertEqual(resolve(url).func,done_extra)

    def test_login_url_resolved(self):
        #Act
        url = reverse('login')
        #Assert
        self.assertEqual(resolve(url).func,login)

    def test_institutions_url_resolved(self):
        #Act
        url = reverse('institutions')
        #Assert
        self.assertEqual(resolve(url).func,institutions)

    def test_child_url_resolved(self):
        #Act
        url = reverse('child')
        #Assert
        self.assertEqual(resolve(url).func,child)

    def test_iteacher_dashboard_url_resolved(self):
        #Act
        url = reverse('teacher_dashboard')
        #Assert
        self.assertEqual(resolve(url).func,teacher_dashboard)

    def test_teacher_dashboard_my_class_url_resolved(self):
        #Act
        url = reverse('my_class')
        #Assert
        self.assertEqual(resolve(url).func,my_class)

    def test_teacher_dashboard_teacher_details_url_resolved(self):
        #Act
        url = reverse('teacher_details')
        #Assert
        self.assertEqual(resolve(url).func,teacher_details)

    def test_child_delete_url_resolved(self):
        #Act
        url = reverse('child_delete')
        #Assert
        self.assertEqual(resolve(url).func,child_delete)
   
    def test_play_games_url_resolved(self):
        #Act
        url = reverse('play_game')
        self.assertEqual(resolve(url).func,play_game)

    def test_score_board_url_resolved(self):
        #Act
        url = reverse('score_board')
        #Assert
        self.assertEqual(resolve(url).func,score_board)    
            









