from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'chat.views.home', name='home'),
    url(r'^chat/$', TemplateView.as_view(template_name='index.html'), name='chat'),
    url(r'^form/$', 'chat.views.form', name='form'),
    url(r'^login/', 'django.contrib.auth.views.login', {"template_name": "login.html"}, name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
