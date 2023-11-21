from django.test import TestCase
from users.models import CustomUser

class CustomUserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'testpassword',
        }

    def test_create_user(self):
        user_obj = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user_obj.email, self.user_data['email'])
        self.assertEqual(user_obj.username, self.user_data['username'])
        self.assertTrue(user_obj.check_password(self.user_data['password']))

    def test_create_superuser(self):
        superuser_obj = CustomUser.objects.create_superuser(**self.user_data)
        self.assertTrue(superuser_obj.is_superuser)
        self.assertTrue(superuser_obj.is_staff)

    def test_update_user(self):
        user_obj = CustomUser.objects.create_user(**self.user_data)
        updated_data = {
            'email': 'updateduser@example.com',
            'username': 'updateduser',
        }
        for key, value in updated_data.items():
            setattr(user_obj, key, value)
        user_obj.save()

        updated_user = CustomUser.objects.get(pk=user_obj.pk)
        self.assertEqual(updated_user.email, updated_data['email'])
        self.assertEqual(updated_user.username, updated_data['username'])

    def test_query_user(self):
        user_obj = CustomUser.objects.create_user(**self.user_data)
        queried_user = CustomUser.objects.get(pk=user_obj.pk)
        self.assertEqual(queried_user.email, self.user_data['email'])
        self.assertEqual(queried_user.username, self.user_data['username'])

    def test_delete_user(self):
        user_obj = CustomUser.objects.create_user(**self.user_data)
        user_obj.delete()
        self.assertEqual(CustomUser.objects.count(), 0)