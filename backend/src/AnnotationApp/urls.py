from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    url(r'^api/label/$',views.labelApi),
    url(r'^api/label/([0-9]+)$',views.labelApi),
    url(r'^api/exportfile$', views.ExportFile),

    url(r'^savefile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
