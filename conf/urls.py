from django.conf import settings
from django.conf.urls import include, url
from django.http import HttpResponse


def home_view(request):
    return HttpResponse(b'This app is empty')


urlpatterns = [
    # Examples:
    url(r'^$', home_view, name='home'),
    # url(r'^blog/', include('blog.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

