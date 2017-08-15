from rest_framework_bulk.routes import BulkRouter

from . import bulk_views

bulk_router = BulkRouter()

bulk_router.register(r'decisions', bulk_views.BulkDecisionViewSet)
bulk_router.register(r'periods', bulk_views.BulkPeriodViewSet)
bulk_router.register(r'phases', bulk_views.BulkPhaseViewSet)
bulk_router.register(r'results', bulk_views.BulkResultViewSet)
bulk_router.register(r'roles', bulk_views.BulkRoleViewSet)
bulk_router.register(r'runs', bulk_views.BulkRunViewSet)
bulk_router.register(r'runusers', bulk_views.BulkRunUserViewSet)
bulk_router.register(r'scenarios', bulk_views.BulkScenarioViewSet)
bulk_router.register(r'worlds', bulk_views.BulkWorldViewSet)

bulk_urlpatterns = bulk_router.urls
