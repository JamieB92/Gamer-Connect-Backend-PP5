from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='password101.')

    def test_can_display_all_posts(self):
        test = User.objects.get(username='test')
        Post.objects.create(owner=test, post_header='This is a test')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='test', password='password101.')
        response = self.client.post('/posts/', {'post_header': 'Test Header'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'post_header': 'Test Header'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

