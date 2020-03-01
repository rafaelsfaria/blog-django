from django.test import TestCase
from .models import Post, Category
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


def create_user(name, email, password):
    return User.objects.create_user(username=name, email=email, password=password)


def create_category(name, slug):
    return Category.objects.create(name=name, slug=slug)


def create_post(title, content, category, author, pub_date):
    return Post.objects.create(title=title, content=content, category=category, author=author, pub_date=pub_date)

# Create your tests here.
# Models
class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_category('Test category', 'test_category')

    def test_category_name(self):
        category = Category.objects.get(id=1)
        name = category._meta.get_field('name').verbose_name
        self.assertEqual(name, 'name')

    def test_category_slug(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_first_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_category_str_method(self):
        category = Category.objects.get(id=1)
        expected = 'Test category'
        self.assertEqual(expected, str(category))

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = create_user('test_user', 'rafaelsanfaria@gmail.com', 'Rxafd68271@')
        category = create_category('Test category', 'test_category')
        create_post('Test title', 'test content', category, user, datetime.datetime.now())

    def test_post_title(self):
        post = Post.objects.get(id=1)
        title = post._meta.get_field('title').verbose_name
        self.assertEqual(title, 'title')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        content = post._meta.get_field('content').verbose_name
        self.assertEquals(content, 'content')

    def test_post_str_method(self):
        post = Post.objects.get(id=1)
        expected = 'Test title'
        self.assertEqual(expected, str(post))

#Views