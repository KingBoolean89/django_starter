from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  
from django.contrib import admin
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name='home')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
