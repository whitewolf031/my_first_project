from django.contrib import admin
from django.urls import path, include
from my_app.views import *
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("persons/", PersonListApiView.as_view(), name="odamalrni korish"),
    path("person/create/", PersonCreateApiView.as_view(), name="Odam yaratish"),

    #products
    path("products/", include("products.urls"), name="Products_update")
]
