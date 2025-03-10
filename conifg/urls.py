"""
URL configuration for conifg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import status
from django.http import JsonResponse

# Healthcheck endpoint
def healthcheck(request):
    return JsonResponse(
        data={"message": "task manager is running"},
        status=status.HTTP_200_OK,
    )


router = DefaultRouter()

api_versions = {
    "v1": [
        ("users.urls", "users/"),
        ("tasks.urls", "tasks/"),
    ]
}

urlpatterns = [
    path("", healthcheck, name="healthcheck"),
    path("admin/", admin.site.urls),
]

for version, routes in api_versions.items():
    for app_url, base_path in routes:
        urlpatterns.append(path(f"api/{version}/{base_path}", include(app_url)))
