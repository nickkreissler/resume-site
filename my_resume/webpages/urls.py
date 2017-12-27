from django.conf.urls import url
from webpages.views import home, about, resume
urlpatterns = [

    url(r'^$', resume, name = 'resume'),
]
