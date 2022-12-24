from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account_app.urls')),
    path('', include('quiz_app.urls')),
]
