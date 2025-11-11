from django.contrib import admin
from django.urls import path
from my_app.views import PersonListApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("persons/", PersonListApiView.as_view(), name="Person"),
]
