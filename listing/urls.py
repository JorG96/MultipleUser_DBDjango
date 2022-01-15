from django.urls import path
from .views import ListingDetailView, ManageListingView

urlpatterns=[
    path('manage',ListingDetailView.as_view()),
    path('detail',ManageListingView.as_view()),
    
]