
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('ledger.urls', namespace="ledger")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)