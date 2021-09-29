from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_view, name='course'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$',views.step_detail, name='stepdet'),
    url(r'(?P<pk>\d+)/$',views.course_detail, name='coursedet'), 
]

# putting the step_detail before the course_detail so as to be sure to capture both.