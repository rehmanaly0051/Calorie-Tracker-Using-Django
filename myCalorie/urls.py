from django.contrib import admin
from django.urls import path, include
from myApp import views  # Assuming your custom login view is in `views.py`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
]
