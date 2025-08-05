from django.contrib import admin
from django.urls import path, include # include が import されていない場合は追加

# ...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('main.urls')), # これを追加
]