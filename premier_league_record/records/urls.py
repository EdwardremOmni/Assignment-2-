from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, dump_august, import_fixtures, august_fixtures, AugustFixtureViewSet, dump_august

router = DefaultRouter()
router.register(r'matches', MatchViewSet)
router.register(r'august-fixtures', AugustFixtureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import-fixtures/', import_fixtures, name='import-fixtures'),
    path('august-fixtures/', august_fixtures, name='august-fixtures'),
    path('dump-august/', dump_august, name='dump-august'),

]
