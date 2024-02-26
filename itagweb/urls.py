from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = (
    [
    path("admin/", admin.site.urls),
    path("", include("web.urls", namespace="web")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Itag Administration"
admin.site.site_title = "Itag Admin Portal"
admin.site.index_title = "Welcome to Itag Admin Portal"