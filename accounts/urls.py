from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    path("account/", views.AccountUpdateView.as_view(), name="account"),
    path("account/password/", views.AccountPasswordView.as_view(), name="account_password"),
    
    # USERS
    path("users/", views.UserListView.as_view(), name="user_list"),
    path("users/create/", views.UserCreateView.as_view(), name="user_create"),
    path("users/<int:pk>/edit/", views.UserUpdateView.as_view(), name="user_update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
    path("users/<int:pk>/permissions/", views.UserPermissionsView.as_view(), name="user_permissions"),
]