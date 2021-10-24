import datetime
from django.http import response
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.
def create_question (question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests (TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_q = Question(pub_date=time)
        self.assertIs(future_q.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_q = Question(pub_date=time)
        self.assertIs(old_q.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_q = Question(pub_date=time)
        self.assertIs(recent_q.was_published_recently(), True)

class QuestionIndexViewTests(TestCase) :
    def test_no_questions(self) :
        response = self.client.get(reverse('pos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No data available.")
        self.assertQuerysetEqual(response.context['lquestion_list'], [])
    
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on 
        the index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('pos:index'))
        self.assertQuerysetEqual(response.context['lquestion_list'], [question])

    def test_future_question (self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('pos:index'))
        self.assertContains(response, "No pos available.")
        self.assertQuerysetEqual(response.context['lquestion_list'], [])

    def test_future_question_and_past_question (self) :
        question = create_question(question_text="Past question?", days=30)
        response = self.client.get(reverse('pos:index'))
        self.assertQuerysetEqual(response.context['lquestion_list'], [question])
    
    def test_two_past_questions (self):
        q1 = create_question(question_text="Past question 1.", days=-30)
        q2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('pos:index'))
        self.assertQuerysetEqual(response.context['lquestion_list'], [q2, q1])
    
class QuestionDetailViewTests(TestCase) :
    def test_future_question (self):
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('pos:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question (self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('pos:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionResultsViewTests(TestCase) :
    def test_future_question (self):
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('pos:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question (self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('pos:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)