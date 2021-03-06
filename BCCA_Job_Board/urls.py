"""BCCA_Job_Board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("post-job", views.PostJob.as_view(), name='post-job'),
    path("az", views.AToZ.as_view(), name='az'),
    path("newold", views.NewOld.as_view(), name='newold'),
    path("oldnew", views.OldNew.as_view(), name='oldnew'),
    path('details/<int:id>', views.JobDetails.as_view(), name='details'),
    # path('apply/<int:id>', views.ApplyToJob.as_view(), name='apply'),
    path('comment/<int:id>', views.Comment.as_view(), name='comment'),
    path('admin', views.Admin.as_view(), name='admin'),
    path('comment/<int:id>/delete', views.CommentDelete.as_view(), name='comment-delete'),
    path('post-job/<int:id>/delete', views.DeleteJob.as_view(), name='delete-job'),
]
