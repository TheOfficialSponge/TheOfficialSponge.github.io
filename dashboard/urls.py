from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('spongebob', views.sb, name="sb"),
    path('patrick', views.p, name="p"),
    path('mr.krabs', views.k, name="k"),
    path('squidward', views.sq, name="sq"),
    path('fred', views.f, name="f"),
    path('plankton', views.pl, name="pl"),
    path('gary', views.g, name="g"),
    path('sandy', views.s, name="s"),
    path('admin/', admin.site.urls)    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
