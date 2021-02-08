
from django.contrib import admin
from django.urls import path
from Enquery import views

urlpatterns = [
    path('',views.Enquery_data),
    path('admin/', admin.site.urls),
]
