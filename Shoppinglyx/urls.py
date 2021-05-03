
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('user/', admin.site.urls),
    
    path('', include('app.urls')),
    path('', include('django.contrib.auth.urls'))  
    
]
