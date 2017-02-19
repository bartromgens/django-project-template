from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from website.views import UserProfileView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='website/index.html'), name='homepage'),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', login_required(UserProfileView.as_view()), name='userprofile'),

    url(r'^accounts/', include('registration.backends.simple.urls')),  # the django-registration module

    url(r'^admin/', admin.site.urls),
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
