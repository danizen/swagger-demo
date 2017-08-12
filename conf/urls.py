from django.conf import settings
from django.conf.urls import include, url
from django.http import HttpResponse
from rest_framework_swagger.views import get_swagger_view


def home_view(request):
    return HttpResponse(b'This app is empty')


swagger_view = get_swagger_view(title='Pastebin API', url='/api')


urlpatterns = [
    # Examples:
    url(r'^$', home_view, name='home'),
    url(r'^swagger/', swagger_view, name='swagger'),
    # url(r'^blog/', include('blog.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

