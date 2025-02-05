from django.conf import settings
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from pagesstatic.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('stat/', include('pagesstatic.urls', 'pagesstatic')),
    path('about/', include('abcompany.urls', 'about')),
    path('projects/', include('projects.urls', 'projects')),
    path('portfolio/', include('portfolio.urls', 'portfolio')),
    path('news/', include('news.urls', 'news')),
    path('contacts/', include('contacts.urls', 'contacts')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('stat/', include('pagesstatic.urls')),
    path('about/', include('abcompany.urls')),
    path('projects/', include('projects.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('news/', include('news.urls')),
    path('contacts/', include('contacts.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
