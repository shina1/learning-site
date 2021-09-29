from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.contrib.auth.models import User
from django.utils import timezone
from .views  import course_detail
from .models import Course
# Create your tests here.

class CourseModelTests(TestCase):
    def setUp(self):
       self.course = Course.objects.create(
             title='Python Regular Expressions',
            description='Learn the secrets of python regex'
        )
    #  a test that creates a course and uses the right created_at time

    def test_course_create(self):
        course = Course.objects.create(
            title='Python Regular Expressions',
            description='Learn the secrets of python regex'
          )
        now = timezone.now()
        self.assertLessEqual(course.created_at,now)

    def test_course_detials_view_success_status_code(self):
        url = reverse('coursedet', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_step_detials_view_success_status_code(self):
        url = reverse('stepdet', kwargs={'course_pk':4,'step_pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)    