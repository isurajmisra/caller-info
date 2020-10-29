from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/users/', views.UserView.as_view()),
    path('api/v1/users/search', views.SearchUserView.as_view()),
    path('api/v1/auth/login/', views.LoginView.as_view()),
    path('api/v1/auth/logout/', views.LogoutView.as_view()),
    path('api/v1/users/<int:id>/', views.UserDetailView.as_view()),
    path('api/v1/users/<int:user_id>/contacts/', views.ContactListView.as_view()),
    path('api/v1/users/<int:user_id>/contacts/<int:contact_id>/', views.UserDetailView.as_view()),
    path('api/v1/users/<int:user_id>/spam_contacts/', views.SpamView.as_view()),
    path('api/v1/users/<int:user_id>/spam_contacts/<int:spam_id>/', views.UserDetailView.as_view()),
]