from django.contrib import admin
from django.urls import include, path

admin.site.site_title = 'stuDB' 
admin.site.site_header = 'stuDB' 
admin.site.index_title = 'menu'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studb.urls')),
]