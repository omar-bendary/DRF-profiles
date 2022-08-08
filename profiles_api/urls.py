from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api.views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView

router = DefaultRouter()
router.register('hello_viewset', HelloViewSet, base_name='hello_viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello_view/', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
