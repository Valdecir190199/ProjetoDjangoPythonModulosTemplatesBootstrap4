from django.urls import path
from .views import *

urlpatterns = [
	path('', PrincipalView.as_view(), name="index"),
]
