from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("login/", include("rest_framework.urls")),
    re_path(r"^.*$", include("frontend.urls"))
]
