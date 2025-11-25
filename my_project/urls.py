from django.contrib import admin
from django.urls import path, include
from my_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),  # users/, me/, create user va h.k
    path('api/auth/', include('djoser.urls.authtoken'))

    # path("", include("accaounts.urls")),
    #products
    # path("products/", include("products.urls"), name="Products_update"),
    # # person
    # path("person/", include("my_app.urls")),
]
