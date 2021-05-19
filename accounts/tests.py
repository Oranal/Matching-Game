from django.test import TestCase
from django.test import tag
from django.urls import resolve
from django.urls import reverse
from accounts.models import Account
from accounts.apps import AccontsConfig
from accounts.views import *
from accounts.forms import FormLogin, KindergardenForm, ChildForm, ChildEditForm, SingleForm, DoubleForm


# TEST MODELS:

@tag('unit-test')
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


# TEST URLS:

@tag('unit-test')
class AccountsUrlsTest(TestCase):
    def test_admin_dashboard_url_resolved(self):
        # Act
        url = reverse('admin_dashboard')
        # Assert
        self.assertEqual(resolve(url).func, admin_dashboard)

    def test_games_url_resolved(self):
        # act
        url = reverse('games')
        # Assert
        self.assertEqual(resolve(url).func, games)

    def test_difficulty_url_resolved(self):
        # Act
        url = reverse('difficulty')
        # Assert
        self.assertEqual(resolve(url).func, difficulty)

    def test_new_game_url_resolved(self):
        # Act
        url = reverse('new_game')
        # Assert
        self.assertEqual(resolve(url).func, new_game)

    def test_game_info_url_resolved(self):
        # Act
        url = reverse('game_info')
        # Assert
        self.assertEqual(resolve(url).func, game_info)

    def test_game_topic_url_resolved(self):
        # Act
        url = reverse('game_topic')
        # Assert
        self.assertEqual(resolve(url).func, game_topic)

    def test_extra_card_url_resolved(self):
        # Act
        url = reverse('extra_card')
        # Assert
        self.assertEqual(resolve(url).func, extra_card)

    def test_done_extra_url_resolved(self):
        # Act
        url = reverse('done_extra')
        # Assert
        self.assertEqual(resolve(url).func, done_extra)

    def test_login_url_resolved(self):
        # Act
        url = reverse('login')
        # Assert
        self.assertEqual(resolve(url).func, login)

    def test_institutions_url_resolved(self):
        # Act
        url = reverse('institutions')
        # Assert
        self.assertEqual(resolve(url).func, institutions)

    def test_child_url_resolved(self):
        # Act
        url = reverse('child')
        # Assert
        self.assertEqual(resolve(url).func, child)

    def test_iteacher_dashboard_url_resolved(self):
        # Act
        url = reverse('teacher_dashboard')
        # Assert
        self.assertEqual(resolve(url).func, teacher_dashboard)

    def test_teacher_dashboard_my_class_url_resolved(self):
        # Act
        url = reverse('my_class')
        # Assert
        self.assertEqual(resolve(url).func, my_class)

    def test_teacher_dashboard_teacher_details_url_resolved(self):
        # Act
        url = reverse('teacher_details')
        # Assert
        self.assertEqual(resolve(url).func, teacher_details)

    def test_child_delete_url_resolved(self):
        # Act
        url = reverse('child_delete')
        # Assert
        self.assertEqual(resolve(url).func, child_delete)

    def test_play_games_url_resolved(self):
        # Act
        url = reverse('play_game')
        self.assertEqual(resolve(url).func, play_game)

    def test_score_board_url_resolved(self):
        # Act
        url = reverse('score_board')
        # Assert
        self.assertEqual(resolve(url).func, score_board)

    def test_search_url_resolved(self):
        # Act
        url = reverse('search')
        # Assert
        self.assertEqual(resolve(url).func, search)


# TEST FORMS:

@tag('unit-test')
class FormLoginTest(TestCase):
    def setUp(self):
        self.form_data = {'UserName': 'userNameTest',
                          'Password': 'passwordTest'}
        self.form = FormLogin(data=self.form_data)

    def test_UserName_required(self):
        # Assert
        self.assertTrue(self.form.fields['UserName'].required)

    def test_Password_required(self):
        # Assert
        self.assertTrue(self.form.fields['Password'].required)


class KindergardenFormTest(TestCase):
    def setUp(self):
        self.form_data = {'FirstName': 'FirstNameTest',
                          'LastName': 'LastNameTest', 'Institution': 'InstitutionTest'}
        self.form = KindergardenForm(data=self.form_data)

    def test_FirstName_required(self):
        # Assert
        self.assertTrue(self.form.fields['FirstName'].required)

    def test_LastName_required(self):
        # Assert
        self.assertTrue(self.form.fields['LastName'].required)

    def test_Institution_required(self):
        # Assert
        self.assertTrue(self.form.fields['Institution'].required)


class ChildFormTest(TestCase):
    def setUp(self):
        self.form_data = {'FirstName': 'FirstNameTest',
                          'LastName': 'LastNameTest', 'role': 'Child', 'rating': 0}
        self.form = ChildForm(data=self.form_data)

    def test_FirstName_required(self):
        # Assert
        self.assertTrue(self.form.fields['FirstName'].required)

    def test_LastName_required(self):
        # Assert
        self.assertTrue(self.form.fields['LastName'].required)

    def test_get_role_func(self):
        self.assertEqual(self.form.get_role(), "Child")

    def test_get_rating_func(self):
        self.assertEqual(self.form.get_rating(), 0)


class ChildEditFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            'Institution': 'InstitutionTest', 'rating': 'ratingTest'}
        self.form = ChildEditForm(data=self.form_data)

    def test_Institution_required(self):
        # Assert
        self.assertTrue(self.form.fields['Institution'].required)

    def test_rating_required(self):
        # Assert
        self.assertTrue(self.form.fields['rating'].required)


class SingleFormTest(TestCase):
    def setUp(self):
        self.form_data = {'data': 'dataTest'}
        self.form = SingleForm(data=self.form_data)

    def test_data_required(self):
        # Assert
        self.assertTrue(self.form.fields['data'].required)


# TEST VIEWS:

class LoginTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        # Act
        response = self.client.get('')
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        # Act
        response = self.client.get(reverse(login))
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        # Act
        response = self.client.get(reverse('login'))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    @tag('unit-test')
    def test_view_contains_form(self):
        # Act
        response = self.client.get(reverse('login'))
        # Assert
        self.assertIsNotNone(response.context['form'])

    @tag('unit-test')
    def test_administrator_login_user(self):
        # Arrange
        Account.objects.create(username='test_administrator_login_user_name',
                               first_name='first name', last_name='last name',
                               password="administratorPassword")
        form_data = {'UserName': 'test_administrator_login_user_name',
                     'Password': 'administratorPassword'}

        # Act
        response = self.client.post(
            reverse('login'), data=form_data, follow=True)

        # assert
        self.assertEqual(response.status_code, 200)

    #     @tag('unit-test')
    # def test_view_signup_child(self):
    #     # Arrange
    #      Account.objects.create(username='usernameTest', first_name='first name',
    #                             last_name='last name', password="ChildPassword")
    #     form_data = {'username': 'usernameTest','password': 'ChildPassword'}
    #     # Act
    #     response = self.client.post('login', data=form_data, follow=True)

    #     # Assert
    #     self.assertEqual(response.status_code, 200)


class institutionsTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        # Act
        response = self.client.get('')
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        # Act
        response = self.client.get(reverse(institutions))
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        # Act
        response = self.client.get(reverse('institutions'))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/institutions.html')

    @tag('unit-test')
    def test_view_contains_form(self):
        # Act
        response = self.client.get(reverse('institutions'))
        # Assert
        self.assertIsNotNone(response.context['form'])


class childTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        # Act
        response = self.client.get('')
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        # Act
        response = self.client.get(reverse(child))
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        # Act
        response = self.client.get(reverse('child'))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/games.html')

    # didn't use any form in this view

    # @tag('unit-test')
    # def test_view_contains_form(self):
    #     # Act
    #     response = self.client.get(reverse('ChildForm'))
    #     # Assert
    #     self.assertIsNotNone(response.context['form'])


class adminDashboardTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        # Act
        response = self.client.get('')
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        # Act
        response = self.client.get(reverse(admin_dashboard))
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        # Act
        response = self.client.get(reverse('admin_dashboard'))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/admin_dashboard.html')

    @tag('unit-test')
    def test_view_contains_form(self):
        # Act
        response = self.client.get(reverse('admin_dashboard'))
        # Assert
        self.assertIsNotNone(response.context['form'])


class teacher_detailsTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        # Act
        response = self.client.get('')
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        # Act
        response = self.client.get(reverse(teacher_details))
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        # Act
        response = self.client.get(reverse('teacher_details'))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/games.html')

    # didn't use any form in this view

    # @tag('unit-test')
    # def test_view_contains_form(self):
    #     # Act
    #     response = self.client.get(reverse('teacher_details'))
    #     # Assert
    #     self.assertIsNotNone(response.context['form'])


class child_deleteTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        # Act
        response = self.client.get('')
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        # Act
        response = self.client.get(reverse(child_delete))
        # Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        # Act
        response = self.client.get(reverse('child_delete'))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/games.html')

    # didn't have any form in this template

    # @tag('unit-test')
    # def test_view_contains_form(self):
    #     # Act
    #     response = self.client.get(reverse('child_delete'))
    #     # Assert
    #     self.assertIsNotNone(response.context['forms.ChildForm'])


# TEST APP:

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        # Assert
        self.assertEqual(AccontsConfig.name, "acconts")
