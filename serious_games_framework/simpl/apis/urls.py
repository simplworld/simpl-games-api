from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'decision', views.DecisionViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'period', views.PeriodViewSet)
router.register(r'phase', views.PhaseViewSet)
router.register(r'result', views.ResultViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'round', views.RoundViewSet)
router.register(r'run', views.RunViewSet)
router.register(r'scenario', views.ScenarioViewSet)
router.register(r'world', views.WorldViewSet)

router.register(r'webhook', views.WebhookViewSet)
router.register(r'webhooklog', views.WebhookLogViewSet)

urlpatterns = router.urls
