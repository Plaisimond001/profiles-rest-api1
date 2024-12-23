from django.conf.urls import url

from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewset)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
#    url(r'^login/$', views.LoginViewSet.as_view(), name='login'),  # Ajout de la route pour login
    url(r'', include(router.urls))
]
