from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('upload', views.upload, name='upload'),
    path('like', views.like, name='like'),
    path('bookmarks', views.bookmarks, name='bookmarks'),
    path('views', views.view, name='view'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('follow', views.follow, name='follow'),
]