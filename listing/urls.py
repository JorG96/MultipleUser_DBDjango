from django.urls import path
from .views import ManageListing

urlpatterns=[
    path('manage',ManageListing.as_view()),
    
]