from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, import_fixtures

router = DefaultRouter()
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import-fixtures/', import_fixtures, name='import-fixtures'),
]
