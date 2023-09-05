from django.test import TestCase

from rest_framework.test import APITestCase
from .models import Exhibition, Illustration, UserProfile
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from allauth.account.models import EmailAddress
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token                                  
from django.test import Client

# Create your tests here.

class ExhibitionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.artist_user = User.objects.create_user(
          username='testartistuser',
          password='testpassword',
          email='test@example.com'
        )
        self.visitor_user = User.objects.create_user(
          username='testvisitoruser',
          password='testpassword',
          email='test@example.com'
        )
        self.artist_profile = UserProfile.objects.create(
            user=self.artist_user,
            is_artist=True
        )
        self.visitor_profile = UserProfile.objects.create(
            user=self.visitor_user,
            is_artist=False
        )
        self.exhibition_data = {
            'name': 'Mi Exposicion',
            'theme': 'Tematica de la exposicion',
            'room_width': 5,
            'room_length': 10,
            'wall_color': '#ffffff',
            'artist': self.artist_profile.id
        }
        
    def test_create_exhibition_authenticated(self):
        token, created = Token.objects.get_or_create(user=self.artist_user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('exhibition-list') 
        
        response = self.client.post(url, self.exhibition_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_exhibition_unauthenticated(self):
        url = reverse('exhibition-list') 

        response = self.client.post(url, self.exhibition_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_exhibition_visitor(self):
        token, created = Token.objects.get_or_create(user=self.visitor_user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('exhibition-list') 

        response = self.client.post(url, self.exhibition_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ChangeProfileTypeViewTestCase(TestCase):
    def setUp(self):
      self.client = APIClient()
      self.user = User.objects.create_user(
          username='testuser',
          password='testpassword',
          email='test@example.com'
        )
      self.user_profile = UserProfile.objects.create(
          user=self.user,
          is_artist=True 
      )
      self.token, _ = Token.objects.get_or_create(user=self.user)
      self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_change_profile_type_to_non_artist(self):
      url = reverse('change_profile')  
      response = self.client.patch(url, format='json')

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.user_profile.refresh_from_db()
      self.assertFalse(self.user_profile.is_artist)

    def test_change_profile_type_to_artist(self):
        self.user_profile.is_artist = False
        self.user_profile.save()

        url = reverse('change_profile')  
        response = self.client.patch(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user_profile.refresh_from_db()
        self.assertTrue(self.user_profile.is_artist)

    def test_change_profile_type_unauthenticated(self):
        self.client.credentials()  
        url = reverse('change_profile')  
        response = self.client.patch(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserTestCase(TestCase): 
    def setUp(self):
      self.client = APIClient()
      self.user = User.objects.create_user(
        username='testuser',
        password='testpassword',
        email='test@example.com'
      )

    def test_login(self):
      self.assertTrue(self.client.login(username="testuser", password= "testpassword"))
    def test_login_false(self):
      self.assertFalse(self.client.login(username="testuser", password= "testpassword1"))