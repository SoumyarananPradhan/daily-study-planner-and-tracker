from rest_framework.routers import DefaultRouter
from .api_views import StudySessionViewSet

router = DefaultRouter()
router.register("sessions", StudySessionViewSet, basename="sessions")

urlpatterns = router.urls
