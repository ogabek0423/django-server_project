
from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ThankYouView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('products.urls')),
    path('', IndexView.as_view(), name='index'),
    path('thank/', ThankYouView.as_view(), name='thank'),
    path(r'mdeditor/', include('mdeditor.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


