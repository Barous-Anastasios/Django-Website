from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from website import urls

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/en', permanent=True), name='index'),
	url(r'^(?P<lang>[a-zA-Z]{2})/', include('website.urls')),
    url(r'^cms/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)