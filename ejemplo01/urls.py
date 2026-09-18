from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='app1/')),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
]