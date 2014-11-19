from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'writing_sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'quiz.views.home_page', name='home'),
    url(r'^sets/(.*)/learn$', 'quiz.views.learn_page', name='learn'),
    url(r'^admin/', include(admin.site.urls)),
)
