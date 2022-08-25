from django.urls import path
from .views import second_include, works_include
urlpatterns = [
    path("", works_include),  # /modals/
    path("second/",second_include)
]