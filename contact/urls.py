from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ListContacts.as_view()),
    path('contact/<int:pk>/', views.ContactDetail.as_view())
]