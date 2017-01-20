from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views


urlpatterns = patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
)
