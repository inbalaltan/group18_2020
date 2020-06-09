from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user_login = {'username': 'test','password': '!!Test123'}
        self.user = User.objects.create_user(**self.user_login)
        self.user.save()
        self.post = Post.objects.create(title = 'test',
         content = 'Test test',
          author = self.user )
        self.post.save()
        self.id = self.post.id

    def test_title(self):
        post = Post.objects.get(id=self.id)
        self.assertEqual(post.title, 'test')

    def test_title_max_length(self):
        post = Post.objects.get(id=self.id)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_content(self):
        post = Post.objects.get(id=self.id)
        self.assertEqual(post.content, 'Test test')

    def test_author(self):
        post = Post.objects.get(id=self.id)
        self.assertEqual(post.author, self.user)

    def test_title_missing_field(self):
        try:
            post = Post.objects.create(title = None,
            content = 'Test test',
            author = self.user )
            post.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: home_post.title")

    def test_content_missing_field(self):
        try:
            post = Post.objects.create(title = 'test',
            content = None,
            author = self.user )
            post.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: home_post.content")


    def test_author_missing_field(self):
        try:
            post = Post.objects.create(title = 'test',
            content = 'test Test',
            author = None )
            post.save()
        except Exception as err:
            self.assertEqual(str(err), "NOT NULL constraint failed: home_post.author_id")