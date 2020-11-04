from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("enrollment", EnrollmentViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("group", GroupViewSet)
router.register("module", ModuleViewSet)
router.register("course", CourseViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("recording", RecordingViewSet)
router.register("event", EventViewSet)
router.register("lesson", LessonViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
