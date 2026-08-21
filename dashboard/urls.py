from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    # DASHBOARD HOME
    path("", views.DashboardHomeView.as_view(), name="home"),

    # MEMBERS
    path("members/", views.MemberListView.as_view(), name="members"),
    path("members/create/", views.MemberCreateView.as_view(), name="member_create"),
    path("members/<int:pk>/edit/", views.MemberUpdateView.as_view(), name="member_edit"),
    path("members/<int:pk>/delete/", views.MemberDeleteView.as_view(), name="member_delete"),

    # ARTICLES
    path("articles/", views.ArticleListView.as_view(), name="articles"),
    path("articles/create/", views.ArticleCreateView.as_view(), name="article_create"),
    path("articles/<int:pk>/edit/", views.ArticleUpdateView.as_view(), name="article_edit"),
    path("articles/<int:pk>/delete/", views.ArticleDeleteView.as_view(), name="article_delete"),

    # ARTICLE CATEGORIES
    # path("categories/", views.ArticleCategoryListView.as_view(), name="categories"),
    path("categories/create/", views.ArticleCategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/edit/", views.ArticleCategoryUpdateView.as_view(), name="category_edit"),
    path("categories/<int:pk>/delete/", views.ArticleCategoryDeleteView.as_view(), name="category_delete"),

    path("categories/", views.ArticleCategoryManageView.as_view(), name="categories"),

    # ACTIVITIES
    path("activities/", views.ActivityListView.as_view(), name="activities"),
    path("activities/create/", views.ActivityCreateView.as_view(), name="activity_create"),
    path("activities/<int:pk>/edit/", views.ActivityUpdateView.as_view(), name="activity_update"),
    path("activities/<int:pk>/delete/", views.ActivityDeleteView.as_view(), name="activity_delete"),

    # CONTACT MESSAGES
    path("messages/", views.ContactMessageListView.as_view(), name="messages"),
    path("messages/<int:pk>/", views.ContactMessageDetailView.as_view(), name="message_detail"),
    path("messages/<int:pk>/status/", views.ContactMessageStatusView.as_view(), name="message_status"),
    path("messages/<int:pk>/delete/", views.ContactMessageDeleteView.as_view(), name="message_delete"),
]