from django.test import TestCase
from django.contrib.auth import get_user_model
from properties.models import Property

class PropertyModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.property_data = {
            'title': 'Test Property',
            'description': 'This is a test property.',
            'price': 100000.00,
            'bedrooms': 3,
            'bathrooms': 2,
            'sqft': 1500,
            'location': 'Test Location',
            'owner': self.user,
        }

    def test_create_property(self):
        property_obj = Property.objects.create(**self.property_data)
        self.assertEqual(Property.objects.count(), 1)
        self.assertEqual(property_obj.title, self.property_data['title'])
        self.assertEqual(property_obj.owner, self.user)

    def test_update_property(self):
        property_obj = Property.objects.create(**self.property_data)
        updated_data = {
            'title': 'Updated Property',
            'price': 120000.00,
            'bedrooms': 4,
        }
        for key, value in updated_data.items():
            setattr(property_obj, key, value)
        property_obj.save()

        updated_property = Property.objects.get(pk=property_obj.pk)
        self.assertEqual(updated_property.title, updated_data['title'])
        self.assertEqual(updated_property.price, updated_data['price'])
        self.assertEqual(updated_property.bedrooms, updated_data['bedrooms'])

    def test_query_property(self):
        property_obj = Property.objects.create(**self.property_data)
        queried_property = Property.objects.get(pk=property_obj.pk)
        self.assertEqual(queried_property.title, self.property_data['title'])
        self.assertEqual(queried_property.owner, self.user)

    def test_delete_property(self):
        property_obj = Property.objects.create(**self.property_data)
        property_obj.delete()
        self.assertEqual(Property.objects.count(), 0)