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


class PostDetailViewTests(APITestCase):
    """
    Tests for post detail view
    """
    def setUp(self):
        """
        Creates two users and a post each
        """
        user_one = User.objects.create_user(username='userone', password='password101.')
        user_two = User.objects.create_user(username='usertwo', password='password101.')
        Post.objects.create(
            owner=user_one, post_header='user one header', caption='user ones caption'
        )
        Post.objects.create(
            owner=user_two, post_header='user two header', caption='user twos caption'
        )

    def test_retrieve_post_with_valid_post_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['post_header'], 'user one header')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unable_to_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='userone', password='password101.')
        response = self.client.put('/posts/1/', {'post_header': 'This is the new header'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.post_header, 'This is the new header')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_unable_to_edit_others_post(self):
        self.client.login(username='userone', password='password101.')
        response = self.client.put('/posts/2/', {'post_header': 'A new header'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
