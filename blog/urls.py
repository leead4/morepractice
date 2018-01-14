from django.conf.urls import include, url
from django.conf.urls import url, include
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import blogpost.views


urlpatterns = [
    url(r'^$', blogpost.views.index, name='index'),
    url(r'^archive$', blogpost.views.archive, name='archive'),
    url(r'^search_keyword/$', blogpost.views.search_keywords, name='search_keywords'),
    url(r'^popular$', blogpost.views.popular, name='popular'),
    url(r'^blog$', blogpost.views.blog, name='blog'),
    url(r'^projects$', blogpost.views.projects, name='projects'),
    url(r'^filter_blog_by_topic/(?P<topic_type>.+?)$', blogpost.views.filter_blog_by_topic, name='filter_blog_by_topic'),
    url(r'^post/(?P<blog_id>.+?)$', blogpost.views.get_this_post, name='get_this_post'),
    url(r'^catsaregreat/', admin.site.urls)
    ] 





