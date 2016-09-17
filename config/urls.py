from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^', include('apps.customer.urls')),
    url(settings.ADMIN_URL, include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    url(r'^', include('apps.dashboard.urls')),
    url(r'^admin/', include('apps.client.urls')),
    url(r'^admin/', include('apps.taller.urls')),
    url(r'^admin/', include('core.urls')),
    url(r'^quotation/', include('apps.taller.urls')),
    url(settings.ADMIN_URL, include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]