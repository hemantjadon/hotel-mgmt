from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = 'Hotel Management System'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
