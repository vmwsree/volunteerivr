# Third Party Stuff
from rest_framework.routers import DefaultRouter

# Volunteer  IVR Management Stuff
from voulnteerivr.base.api.routers import SingletonRouter
from voulnteerivr.users.api import CurrentUserViewSet
from voulnteerivr.users.auth.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, base_name='auth')
singleton_router.register('me', CurrentUserViewSet, base_name='me')

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
