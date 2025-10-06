from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("AML/main", views.main_page, name="main_page"),
]
