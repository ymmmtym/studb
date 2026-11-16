import datetime

from django.contrib import admin
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question, Textbook


class TextbookModelTests(TestCase):
    def test_was_published_recently_with_recent_pub_date(self):
        textbook = Textbook(title='recent', publisher='p', pub_date=timezone.now())
        self.assertIs(textbook.was_published_recently(), True)

    def test_was_published_recently_with_old_pub_date(self):
        pub_date = timezone.now() - datetime.timedelta(days=2)
        textbook = Textbook(title='old', publisher='p', pub_date=pub_date)
        self.assertIs(textbook.was_published_recently(), False)

    def test_str_returns_title(self):
        textbook = Textbook(title='数学I', publisher='p', pub_date=timezone.now())
        self.assertEqual(str(textbook), '数学I')


class QuestionModelTests(TestCase):
    def test_str_returns_title(self):
        question = Question(title='q1', question='1+1?', answer=2)
        self.assertEqual(str(question), 'q1')


class IndexViewTests(TestCase):
    def test_no_textbooks(self):
        response = self.client.get(reverse('studb:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No textbook are available.')

    def test_lists_textbooks_ordered_by_pub_date(self):
        old = Textbook.objects.create(
            title='old', publisher='p',
            pub_date=timezone.now() - datetime.timedelta(days=5),
        )
        new = Textbook.objects.create(
            title='new', publisher='p', pub_date=timezone.now(),
        )
        response = self.client.get(reverse('studb:index'))
        self.assertEqual(response.status_code, 200)
        textbooks = list(response.context['textbooks'])
        self.assertEqual(textbooks, [old, new])


class TextbookViewTests(TestCase):
    def test_existing_textbook(self):
        textbook = Textbook.objects.create(
            title='数学I', publisher='東京書籍', pub_date=timezone.now(),
        )
        response = self.client.get(reverse('studb:textbook', args=[textbook.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '数学I')

    def test_missing_textbook_returns_404(self):
        response = self.client.get(reverse('studb:textbook', args=[999]))
        self.assertEqual(response.status_code, 404)


class AdminRegistrationTests(TestCase):
    def test_models_are_registered(self):
        self.assertIn(Textbook, admin.site._registry)
        self.assertIn(Question, admin.site._registry)
