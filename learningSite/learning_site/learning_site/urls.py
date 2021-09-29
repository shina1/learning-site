from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.urls import path
from django.conf.urls import include, url
from . import views 

urlpatterns = [
    url(r'^courses/',include('courses.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.hello_world, name='helloworld'),
    
    # url(r'^courses/(?P<pk>\d+)/$', courseview.course_detail),
]
# this check if we are in debug mode i.e if debug mode is true and then adds the static file urls.
urlpatterns += staticfiles_urlpatterns()
