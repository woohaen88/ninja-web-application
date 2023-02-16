from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI
from camping.api import router as camping_router

api = NinjaAPI()
api.add_router("/camping/", camping_router, tags=["camping"])


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
