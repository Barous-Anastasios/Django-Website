from django.conf.urls import url
from django.contrib import admin

from website import views as website_views

urlpatterns = [
	url(r'^$', website_views.index, name="index"),
	url(r'^(?P<friendlyurl>[\w\-]+)/$', website_views.regular_page, name="regular_page"),
	url(r'^(?P<friendlyurl>[\w\-]+)/(?P<id>\d+)/$', website_views.regular_sub_page, name="regular_sub_page")
]
