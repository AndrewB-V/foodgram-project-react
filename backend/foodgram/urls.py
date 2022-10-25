from django.urls import include, path

urlpatterns = [
    path("api/", include("foodgram.api_urls")),
]
