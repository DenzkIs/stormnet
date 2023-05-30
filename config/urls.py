from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('products/', include('lesson_model.urls')),
    path('forms/', include('work_forms.urls')),
    path('forms2/', include('home_forms.urls')),
    path('forms3/', include('model_forms.urls')),
    path('my_less_login/', include('less_auth.urls')),
    path('my_home_auth/', include('home_auth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
