from django.contrib import admin
from django.urls import path
from my_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("persons/", PersonListApiView.as_view(), name="odamalrni korish"),
    path("person/create/", PersonCreateApiView.as_view(), name="Odam yaratish")
]
